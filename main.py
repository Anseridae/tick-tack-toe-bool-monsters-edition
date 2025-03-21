from logic.turnSystem import nextTurn

# Todo implement multiplayer, summons that level ups based on sacrifices, rebinding controls, save/loading
# Todo think about letting players pick different spell and monster load-outs and maybe extra passives as well
# Todo add crab passive which does like maybe half damage to the attack when attacked
# Todo add goblin passive to regen mana per turn
# Todo add a check on the heal spell so u can't heal a mob that's already at full health
# Todo refactor the front end to show the game board and each player's field on a subprocess


"""
Todo for FEN string system:
a / denotes an empty space, the number after it is how many more spaces after it are empty.
a capital letter denotes a mob controlled by player 1 a lowercase is controlled by player 2.
the number after the letter is how many times it's been enraged.
an h followed by a number is the monsters current health.
a space followed by another string denotes player 1's field
a space followed bt another string after the player 1s field denotes player 2's field
a $ followed by a number denotes a monsters current stamina.
for now we only care about stamina on the player fields.

Todo figure out how I wanna denote mana and energy.

example FEN string /1W1h2/c2h10/3 /2w1h2#3 /Gh4#0/
example FEN string /1Wh2h2/c2h5/G1h4/1 ch5#0w1h4#3/ G2h4#1


Todo for turn string system:
4 represents that u summoned the same thing on all 3 slots
"S" denotes summoning, whatever letters after the s is what you're trying to summon, they could be on slots 1, 2, or 3
"M" denotes spell casting the <, ^, >, denote which slot you are casting the spell on.
the letter after is what spell you're casting, the number is how many times you're casting it.
"F" denotes attacking the board, the <, ^, >, denotes slot on there field they're attacking, the number is which slot on the board the player attacks.
a number followed by another number denotes attacking the same slot x many more times with the same slot.
attacking an empty slot will just place the monster they're attacking with on that slot and end there turn.
"G" denotes the manual end of a turn without placing a monster on the board.

example turn string Sg4M<e2^h>hG
example turn string Sg1w2F<52^5
example turn string F>5^53Ms<s^S4Ms<Ss<Me4<F<7
"""

"""
Todo for multiplayer:

use TCP websocket, don't have to deal with implementing resend state requests that way and the whole disconnect problem that way.
although if I wanted to use UDP I could have resend state requests being sent by the client and handled by the sever.
and I could have some logic to check if the connection timed out on the client and server.
actually I should double check the socket library and see how it handles connection timeouts on UDP. 

make a parser and a grammar so u can send something like FEN notation up and down the server and clients
convert the game code so far to a client server structure.

make the front end construct a FEN string under the hood and allow for direct sending of the FEN string by the user via a SEND command on the turn screen.
make a parser on the front end that can reed the FEN string and display the current state.
the front end should also double check the string in the SEND command to make sure it's valid before sending anything to the server.

make a parser on the server for checking over the playerTurnInstructions string it got from the client.
first check if it's valid syntax, then check if the instructions are possible, i.e. making sure u can't cast a spell u don't have the mana for.
if syntax is wrong or instructions impossible send a turn failed message and the current state back to the client.
if syntax and instructions correct update the current state and send a waiting for other player message and the current state back to the client.
"""


if __name__ == '__main__':
    nextTurn()
