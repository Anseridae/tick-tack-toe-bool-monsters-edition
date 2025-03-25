from logic.utill import validateInput, getPlayerField
from data.monsters import mobs


def getMonster(valid_list, prompt, player):
    monsterIndex = int(validateInput(valid_list, prompt, player)) - 1
    return player["board"][monsterIndex], monsterIndex


def handleSpell(player, spellFunction, spell: str):
    if player["mana"] < spells[spell]["mana"]:
        input("not enough mana")
    elif not any(player["board"]):
        input("no monsters on board")
    else:
        player["mana"] -= spells[spell]["mana"]
        playerMonstersIndexes = getPlayerField(player["board"])
        selectedMonster = getMonster(playerMonstersIndexes,
                                     f"\nwhich monster do you wish to {spell}?\n{playerMonstersIndexes}\n> ", player)
        spellFunction(selectedMonster)


def heal(player):
    def spellFunction(selectedMonsterHeal):
        selectedMonsterHeal[0]['hp'] = mobs[selectedMonsterHeal[0]["mob"]]["hp"]
    handleSpell(player, spellFunction, "heal")


def enrage(player):
    def spellFunction(selectedMonsterEnrage):
        selectedMonsterEnrage[0]['ap'] *= 2
    handleSpell(player, spellFunction, "enrage")


def sacrifice(player):
    def spellFunction(selectedMonsterSacrifice):
        player["board"][selectedMonsterSacrifice[1]] = {}
    handleSpell(player, spellFunction, "sacrifice")


spells = {
    "heal":      {
        "name":              "heal",
        "description line1": "|fully heal a monster|",
        "description line2": "|                    |",
        "description line3": "|                    |",
        "mana":              3,
        "function":          heal
    },

    "enrage":    {
        "name":              "enrage",
        "description line1": "|double a monster's  |",
        "description line2": "|power for it's next |",
        "description line3": "|attack              |",
        "mana":              5,
        "function":          enrage
    },

    "sacrifice": {
        "name":              "sacrifice",
        "description line1": "|kill a monster on   |",
        "description line2": "|your side           |",
        "description line3": "|                    |",
        "mana":              1,
        "function":          sacrifice
    }
}

spellControls = ((("heal", "h"), "heal"), (("enrage", "e"), "enrage"), (("sacrifice", "s"), "sacrifice"))
