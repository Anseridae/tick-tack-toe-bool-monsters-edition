import os


def displayMonsterDec():
    from data.monsters import mobs, summoningControls
    displayString = ["", "", "", "", "", ""]

    for i in summoningControls:
        infoStrings = [f"energy:  {mobs[i[1]]['energy cost']}",
                       f"health:  {mobs[i[1]]['hp']}",
                       f"stamina: {mobs[i[1]]['stamina']}",
                       f"attack:  {mobs[i[1]]['attack power']}",
                       f"mana:    {mobs[i[1]]['mana']}"]

        displayString[0] += f"\t|{f'{i[1]}': <11}|"
        displayString[1] += f"\t|{f'{infoStrings[0]}': <11}|"
        displayString[2] += f"\t|{f'{infoStrings[1]}': <11}|"
        displayString[3] += f"\t|{f'{infoStrings[2]}': <11}|"
        displayString[4] += f"\t|{f'{infoStrings[3]}': <11}|"
        displayString[5] += f"\t|{f'{infoStrings[4]}': <11}|"

    return displayString


def displaySpellDec():
    from data.spells import spells, spellControls
    displayString = ["", "", "", "", ""]

    for i in spellControls:
        manaString = f"mana cost:  {spells[i[1]]['mana']}"
        displayString[0] += f"\t|{f'{i[1]}': ^20}|"
        displayString[1] += f"\t{spells[i[1]]['description line1']}"
        displayString[2] += f"\t{spells[i[1]]['description line2']}"
        displayString[3] += f"\t{spells[i[1]]['description line3']}"
        displayString[4] += f"\t|{manaString: ^20}|"

    return displayString


def displayPlayersField(player):
    displayString = ["", "", "", ""]

    for i in player["board"]:
        if i:
            mobName = f"{i['mob']}"
            mobHealth = f"health:  {i['hp']}"
            mobStamina = f"stamina: {i['sp']}"
            mobAttack = f"attack:  {i['ap']}"

            displayString[0] += f"  |{mobName: ^11}|  "
            displayString[1] += f"  |{mobHealth: ^11}|  "
            displayString[2] += f"  |{mobStamina: ^11}|  "
            displayString[3] += f"  |{mobAttack: ^11}|  "
        else:
            displayString[0] += "  |           |  "
            displayString[1] += "  |  -empty-  |  "
            displayString[2] += "  |           |  "
            displayString[3] += "  |           |  "
    return displayString


# Todo refactor this
def validateInput(valid_list: list[str], userInputPrompt: str, player: dict | None = None, displaySpells: bool = False, displayTickTackToeBoard: bool = False,
                  displayMonsters: bool = False) -> str:
    os.system("cls")
    if displayTickTackToeBoard:
        boardToDisplay = displayGameBoard()
        print("")
        for i0 in boardToDisplay[0]:
            print(i0)
        print("")
        for i1 in boardToDisplay[1]:
            print(i1)
        print("")
        for i2 in boardToDisplay[2]:
            print(i2)
        print("")

    if player:
        for i in displayPlayersField(player):
            print(i)
    if displaySpells:
        for j in displaySpellDec():
            print(j)
    if displayMonsters:
        for k in displayMonsterDec():
            print(k)
    userInput = input(userInputPrompt)
    if userInput.lower() in valid_list:
        return userInput.lower()
    else:
        return validateInput(valid_list, userInputPrompt, player, displaySpells,  displayTickTackToeBoard, displayMonsters)


def getPlayerField(playerField: dict):
    validPositions = []
    for i, v in enumerate(playerField):
        if v:
            validPositions.append(str(i + 1))
        else:
            validPositions.append(" ")
    return validPositions


def displayGameBoard():
    from gameBoard import gameBoard
    displayString1 = ["", "", "", ""]
    displayString2 = ["", "", "", ""]
    displayString3 = ["", "", "", ""]

    def populateDisplayString(displayString):
        if i:
            mobName = f"{i['mob']}"
            mobHealth = f"health:  {i['hp']}"
            mobAttack = f"attack:  {i['ap']}"
            mobPlayer = i["player"]

            displayString[0] += f"  |{mobName: ^11}|  "
            displayString[1] += f"  |{mobHealth: ^11}|  "
            displayString[2] += f"  |{mobAttack: ^11}|  "
            displayString[3] += f"  |{mobPlayer: ^11}|  "
        else:
            displayString[0] += "  |           |  "
            displayString[1] += "  |  -empty-  |  "
            displayString[2] += "  |           |  "
            displayString[3] += "  |           |  "

    for i in gameBoard[0:3]:
        populateDisplayString(displayString1)
    for i in gameBoard[3:6]:
        populateDisplayString(displayString2)
    for i in gameBoard[6:]:
        populateDisplayString(displayString3)

    return displayString1, displayString2, displayString3




