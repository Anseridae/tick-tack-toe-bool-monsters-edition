import os
from data.players import player1, player2
from logic.attackingSystem import attackOtherPlayersFild, attackGameBoard
from logic.utill import validateInput
from logic.monsterSummoningSystem import summonMonster
from logic.spellCastingSystem import selectSpell


states = {
    "currentTurn": "player 2",
    "isFirstTurn": True
}


def getOtherPlayer():
    return player2 if states["currentTurn"] == "player 1" else player1


def getCurrentPlayer():
    return player1 if states["currentTurn"] == "player 1" else player2


def changeCurrentPlayer():
    states["currentTurn"] = "player 2" if states["currentTurn"] == "player 1" else "player 1"


def nextTurn():
    def regenOtherPlayerMonsterStamina():
        maxStamina = 3
        for i in getOtherPlayer()["board"]:
            if i and i["sp"] < maxStamina:
                i["sp"] += 1

    def handelNextPlayerTurn(player):
        if player["max energy"] > player["energy"]:
            player["energy"] += 1
        regenOtherPlayerMonsterStamina()
        os.system("cls")
        input(f"{player['name']}'s turn\n> ")
        return playerTurn(player)

    changeCurrentPlayer()
    return handelNextPlayerTurn(getCurrentPlayer())


def playerTurn(player: dict):
    action = validateInput(["a", "s", "d", "f", "g"],
                           f"mana: {player['mana']}\n"
                           f"energy: {player['energy']}\n"
                           f"\nwhat would you like to do?\n"
                           f"(a) summon monster\n"
                           f"(s) attack other player's field\n"
                           f"(d) cast spell\n"
                           f"(f) attack the game board\n"
                           f"(g) end turn\n"
                           f"> ",
                           player
                           )

    if action == "a":
        summonMonster(player)

    if action == "s":
        attackOtherPlayersFild(player)

    if action == "d":
        selectSpell(player)

    if action == "f":
        return attackGameBoard(player)

    if action == "g":
        states["isFirstTurn"] = False
        return nextTurn()
