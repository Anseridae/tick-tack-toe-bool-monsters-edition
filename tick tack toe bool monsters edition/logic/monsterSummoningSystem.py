from data.monsters import mobs, summoningControls
from logic.utill import validateInput
import os


def selectEmptyPositionOnBoard(player):
    from logic.turnSystem import playerTurn
    if all(player["board"]):
        os.system("cls")
        input("no empty spaces\n> ")
        return playerTurn(player)

    validPositions = []
    for i, v in enumerate(player["board"]):
        if not v:
            validPositions.append(str(i + 1))
        else:
            validPositions.append(" ")

    return int(validateInput(validPositions,
                             f"\nwhere would you like to summon a monster?\n"
                             f"{validPositions}\n"
                             f"> ",
                             player
                             )) - 1


def handelMob(mob: dict, mobName, player, position):
    if player["energy"] < mobs[mobName]["energy cost"]:
        input("not enough energy")
    else:
        player["energy"] -= mob["energy cost"]
        player["mana"] += mob["mana"]
        player["board"][position] = {
            "mob": mobName,
            "hp":  mob["hp"],
            "sp":  mob["stamina"],
            "ap":  mob["attack power"]
        }


def selectMonster(player, position):
    from logic.turnSystem import playerTurn

    selectedMob = validateInput(["goblins", "goblin", "gob", "g", "wolf", "w", "crab", "c", "shark", "s", "b", "back"],
                                f"\n\nyour energy: {player['energy']}\n\n"
                                f"summoning a monster cost energy\n"
                                f"you gain mana from the monsters you summon\n\n"
                                f"enter the name of a monster to summon it\n"
                                f"enter \"b\" or \"back\" to go back\n"
                                f"> ",
                                displayMonsters=True
                                )

    for i in summoningControls:
        if selectedMob in i[0]:
            handelMob(mobs[i[1]], i[1], player, position)
    return playerTurn(player)


def summonMonster(player):
    pos = selectEmptyPositionOnBoard(player)
    return selectMonster(player, pos)
