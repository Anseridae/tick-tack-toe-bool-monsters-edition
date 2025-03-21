from data.spells import spells, spellControls
from logic.utill import validateInput

# Todo add the ability to cancel casting a spell at any point


def selectSpell(player):
    from logic.turnSystem import playerTurn, states

    if states["isFirstTurn"]:
        input("can't cast spells on first turn\n> ")
        return playerTurn(player)

    selectedSpell = validateInput(["heal", "h", "enrage", "e", "sacrifice", "s", "b", "back"],
                                  f"\n\nyour mana: {player['mana']}\n\n"
                                  f"enter the name of a spell to cast it\n"
                                  f"enter \"b\" or \"back\" to go back\n"
                                  f"> ",
                                  displaySpells=True)

    for i in spellControls:
        if selectedSpell in i[0]:
            spells[i[1]]["function"](player)

    if selectedSpell in ("b", "back"):
        return playerTurn(player)
    return selectSpell(player)
