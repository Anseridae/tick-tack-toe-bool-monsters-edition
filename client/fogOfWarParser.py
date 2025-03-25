

"""
FEN string system:
a / denotes an empty space, the number after it is how many more spaces after it are empty.
a capital letter denotes a mob controlled by player 1 a lowercase is controlled by player 2.
the number after the letter is how many times it's been enraged.
an h followed by a number is the monsters current health.
a space followed by another string denotes player 1's field.
a space followed by another string after the player 1s field denotes player 2's field.
a $ followed by a number denotes a monsters current stamina.
for now we only care about stamina on the player fields.
a % followed by a number denotes the players current mana.
a * followed by a number denotes the players current energy.

example FEN string /1W1h2/c2h10/3 /Gh4$0/%15*0 /1w1h2$3%8*1
example FEN string /1Wh2/c2h5/G1h4/1 G2h4/1$1%6*10 ch5$0w1h4$3/%4*0
"""

# Todo clean this shit up

# testing data
gameBoard = [{}, {}, {},
             {}, {}, {},
             {}, {}, {}
             ]

player1 = {
    "name":       "player 1",
    "mana":       0,
    "max energy": 10,
    "energy":     5,
    "board":      [
        {}, {}, {}
    ],
}

player2 = {
    "name":       "player 2",
    "mana":       0,
    "max energy": 10,
    "energy":     5,
    "board":      [
        {}, {}, {}
    ],
}


def parseFENString(FENString: str):
    parserBoardFieldSlotIndex = 0
    parserState = "empty slot"
    parserBoardFieldState = "game board"

    currentPlayerMana = ""
    currentPlayerEnergy = ""

    currentMonsterPlayer = ""
    currentMonster = ""
    currentMonsterEnrageMultiplier = ""
    currentMonsterHealth = ""
    currentMonsterStamina = ""

    def resetPlayerData():
        nonlocal currentPlayerMana
        nonlocal currentPlayerEnergy
        currentPlayerMana = ""
        currentPlayerEnergy = ""

    def setPlayerData(player):
        player["mana"] = int(currentPlayerMana)
        player["energy"] = int(currentPlayerEnergy)

    def compileMonsterData():
        from data.monsters import mobs

        return {
            "player": currentMonsterPlayer,
            "mob": currentMonster,
            "hp":  int(currentMonsterHealth),
            "sp":  int(currentMonsterStamina) if currentMonsterStamina else 0,
            "ap":  mobs[currentMonster]["attack power"] + (1 + int(currentMonsterEnrageMultiplier)) if currentMonsterEnrageMultiplier else mobs[currentMonster]["attack power"]
        }

    def resetMonsterData():
        nonlocal currentMonsterPlayer
        nonlocal currentMonster
        nonlocal currentMonsterEnrageMultiplier
        nonlocal currentMonsterHealth
        nonlocal currentMonsterStamina
        currentMonsterPlayer = ""
        currentMonster = ""
        currentMonsterEnrageMultiplier = ""
        currentMonsterHealth = ""
        currentMonsterStamina = ""

    def checkMonster(lowerCaseLetter: str):
        # print(lowerCaseLetter)
        nonlocal currentMonster
        match lowerCaseLetter:
            case "w":
                currentMonster = "wolf"
            case "g":
                currentMonster = "goblin"
            case "s":
                currentMonster = "shark"
            case "c":
                currentMonster = "crab"
            case _:
                print("monster not implemented in fog of war parser")

    for char in FENString:
        # print(gameBoard)
        # print(f"the index starts the loop at {parserBoardFieldSlotIndex}")
        # print(f"char is {char}")
        # print(f"parser state is {parserState}")
        # print(f"parser board state is {parserBoardFieldState}")
        if char == '/':
            parserState = "empty slot"
            if not currentMonster and parserBoardFieldState == "game board":
                gameBoard[parserBoardFieldSlotIndex] = {}
            if currentMonster and parserBoardFieldState == "game board":
                gameBoard[parserBoardFieldSlotIndex - 1] = dict(compileMonsterData())
                # print(f"placing monster {currentMonster} at position {parserBoardFieldSlotIndex - 1}")
                resetMonsterData()
                gameBoard[parserBoardFieldSlotIndex] = {}
            if currentMonster and parserBoardFieldState == "player 1 field":
                player1["board"][parserBoardFieldSlotIndex - 1] = dict(compileMonsterData())
                resetMonsterData()
                player1["board"][parserBoardFieldSlotIndex] = {}
            if currentMonster and parserBoardFieldState == "player 2 field":
                player2["board"][parserBoardFieldSlotIndex - 1] = dict(compileMonsterData())
                resetMonsterData()
                player2["board"][parserBoardFieldSlotIndex] = {}
            parserBoardFieldSlotIndex += 1

        elif char.isdigit() and parserState == "empty slot":
            for j in range(int(char)):
                # print(f"j is {j}")
                if parserBoardFieldState == "game board":
                    gameBoard[parserBoardFieldSlotIndex + j] = {}
                if parserBoardFieldState == "player 1 field":
                    player1["board"][parserBoardFieldSlotIndex + j] = {}
                if parserBoardFieldState == "player 2 field":
                    player2["board"][parserBoardFieldSlotIndex + j] = {}

            parserBoardFieldSlotIndex += int(char)
            # print(f"index is now {parserBoardFieldSlotIndex}")
            parserState = ""

        elif char.isupper() and not char == "h":
            if currentMonster and parserBoardFieldState == "game board":
                gameBoard[parserBoardFieldSlotIndex - 1] = dict(compileMonsterData())
                resetMonsterData()

            if currentMonster and parserBoardFieldState == "player 1 field":
                player1["board"][parserBoardFieldSlotIndex - 1] = dict(compileMonsterData())
                resetMonsterData()

            currentMonsterPlayer = "player 1"
            parserState = "monster"
            # print("updating parser state to monster")
            # print(f"parser state is {parserState}")
            checkMonster(char.lower())
            parserBoardFieldSlotIndex += 1

        elif char.islower() and not char == "h":
            if currentMonster and parserBoardFieldState == "game board":
                gameBoard[parserBoardFieldSlotIndex - 1] = dict(compileMonsterData())
                resetMonsterData()

            if currentMonster and parserBoardFieldState == "player 2 field":
                player2["board"][parserBoardFieldSlotIndex - 1] = dict(compileMonsterData())
                resetMonsterData()

            currentMonsterPlayer = "player 2"
            parserState = "monster"
            # print("updating parser state to monster")
            # print(f"parser state is {parserState}")
            checkMonster(char.lower())
            parserBoardFieldSlotIndex += 1

        elif char.isdigit() and parserState == "monster":
            currentMonsterEnrageMultiplier += char

        elif char == "h" and parserState == "monster":
            parserState = "health"

        elif char.isdigit() and parserState == "health":
            currentMonsterHealth += char

        elif char == "$" and parserState == "health":
            parserState = "stamina"

        elif char.isdigit() and parserState == "stamina":
            currentMonsterStamina += char

        elif char == " " and parserBoardFieldState == "game board":
            parserBoardFieldState = "player 1 field"
            parserBoardFieldSlotIndex = 0
            resetPlayerData()

        elif char == " " and parserBoardFieldState == "player 1 field":
            if currentMonster:
                # print(f"index exiting player 1 field {parserBoardFieldSlotIndex}")
                player1["board"][parserBoardFieldSlotIndex - 1] = dict(compileMonsterData())
                resetMonsterData()
            setPlayerData(player1)
            parserBoardFieldState = "player 2 field"
            parserBoardFieldSlotIndex = 0
            resetPlayerData()

        elif char == "%":
            parserState = "mana"

        elif char.isdigit() and parserState == "mana":
            currentPlayerMana += char

        elif char == "*":
            parserState = "energy"

        elif char.isdigit() and parserState == "energy":
            currentPlayerEnergy += char
        # print(f"the index ends the loop at {parserBoardFieldSlotIndex}")
    if FENString:
        if currentMonster:
            player2["board"][parserBoardFieldSlotIndex - 1] = dict(compileMonsterData())
            resetMonsterData()
        setPlayerData(player2)
        resetPlayerData()


def testParser():
    parseFENString("/1W1h2/c2h10/3 /Gh4$0/%15*0 /1w1h2$3%8*1")
    print(gameBoard)
    print()
    print(player1)
    print()
    print(player2)
    print("\n\n")
    parseFENString("/1Wh2/c2h5/G1h4/1 G2h4/1$1%6*10 ch5$0w1h4$3/%4*0")
    print(gameBoard)
    print()
    print(player1)
    print()
    print(player2)
    print("\n\n")


testParser()
