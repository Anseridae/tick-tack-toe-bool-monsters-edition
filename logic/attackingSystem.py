from data.monsters import mobs
from logic.utill import validateInput, getPlayerField
import os


def win(currentPlayer, otherPlayer):
    print(f"{otherPlayer['name']} has died")
    print(f"{currentPlayer['name']} wins! (^-^)")
    input("> ")

# Todo add the ability to cancel an attack at any point and show which mob ur attacking with when targeting another mob


def attackOtherPlayersFild(player):
    from logic.turnSystem import states, getOtherPlayer, playerTurn

    targetPlayer = getOtherPlayer()

    if states["isFirstTurn"]:
        cantAttackOnFistTurn()
    elif not any(player["board"]):
        cantAttackWithoutMonsters()
    elif player["board"][selectedMonster := getMonsterIndex(player)]["sp"] <= 0:
        cantAttackIfMonsterOutOfStamina()
    elif any(targetPlayer["board"]):
        attackMonsters(selectedMonster, getTargetMonsterIndex(targetPlayer), targetPlayer["board"], player)
    else:
        input(f"no monsters remain {targetPlayer['name']}'s field\n> ")
    return playerTurn(player)


def getMonsterIndex(player):
    if any(player["board"]):
        playerMonsters = getPlayerField(player["board"])
        return int(
            validateInput(playerMonsters, f"\nwhich monster do you wish to attack with?\n{playerMonsters}\n> ",
                          player)) - 1


def getTargetMonsterIndex(otherPlayer):
    from logic.turnSystem import getOtherPlayer
    otherPlayerBoard = getPlayerField(getOtherPlayer()["board"])
    return int(
        validateInput(otherPlayerBoard, f"\n\n\nwhat monster would you like to target?\n{otherPlayerBoard}\n> ",
                      otherPlayer)) - 1


def cantAttackOnFistTurn():
    input("can't attack on the first turn\n> ")


def cantAttackWithoutMonsters():
    os.system("cls")
    input("there are no monsters on your field\n> ")


def cantAttackIfMonsterOutOfStamina():
    input("monster is out of stamina\n> ")


def attackMonsters(monsterIndex, targetIndex, targetBoard, player):
    target = targetBoard[targetIndex]
    monster = player["board"][monsterIndex]
    target["hp"] -= monster["ap"]
    monster["sp"] -= 1
    monster["ap"] = mobs[monster["mob"]]["attack power"]
    if target["hp"] <= 0:
        targetBoard[targetIndex] = {}


def placeMonsterOnTickTackToeBoard(boardIndex, player, monsterIndex):
    from gameBoard import gameBoard, checkWin
    from logic.turnSystem import nextTurn, states
    gameBoard[int(boardIndex) - 1] = player["board"][monsterIndex]
    gameBoard[int(boardIndex) - 1]["player"] = player["name"]
    player["board"][monsterIndex] = {}
    states["isFirstTurn"] = False
    print(player["name"])
    if checkWin(player):
        input("you win!\n> ")
    else:
        return nextTurn()


def attackGameBoard(player):
    from logic.turnSystem import playerTurn
    from gameBoard import gameBoard

    if not any(player["board"]):
        cantAttackWithoutMonsters()
        return playerTurn(player)
    else:
        monsterIndex = getMonsterIndex(player)
        boardIndex = validateInput(["1", "2", "3", "4", "5", "6", "7", "8", "9", "b", "back"], "\nwhere would you like to attack?\nattacking an empty space will place your monster on it and end your turn\n\n| 1 | 2 | 3 |\n| 4 | 5 | 6 |\n| 7 | 8 | 9 |\n\nenter \"b\" or \"back\" to go back\n> ", displayTickTackToeBoard=True)
        if boardIndex in ("b", "back"):
            return playerTurn(player)
        elif player["board"][monsterIndex]["sp"] <= 0:
            cantAttackIfMonsterOutOfStamina()
        elif gameBoard[int(boardIndex) - 1]:
            attackMonsters(monsterIndex, int(boardIndex) - 1, gameBoard, player)
        else:
            return placeMonsterOnTickTackToeBoard(boardIndex, player, monsterIndex)
        return playerTurn(player)
