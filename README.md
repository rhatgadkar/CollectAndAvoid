CollectAndAvoid game.

Currently supports a python client using the pygame library.

About the game
--------------
CollectAndAvoid is a game where the player is a green square who tries to
collect light blue squares, while avoiding red squares and the dark blue
square.  The player can move in the north, south, east, and west directions by
using the arrow keys.  Each time the player collects a light blue square, the
player's score increments.  The dark blue square is an AI opponent that also
tries to collect light blue squares.  If the player touches a red square or the
AI opponent, the game is over.  The image below shows the game.

![collectandavoid-gameplay-github](https://user-images.githubusercontent.com/8902454/46189708-c6c4a000-c2a4-11e8-928b-c66e98bb8a28.png)

AI opponent's pathfinding algorithm
-----------------------------------
The AI opponent's pathfinding algorithm is defined in the _get_new_path method
in enemy.py.

The world is divided into many subworlds.  Each subworld has north, south, east,
and west boundaries.  These boundaries are represented by the yellow squares in
the image below.  In the image, a subworld is circled in white.  Each boundary
of a subworld contains five yellow squares.  Within a subworld, some yellow
squares of a boundary overlap with yellow squares of another boundary.  In the
pathfinding algorithm, the AI tries to move in a direction toward the subworld
that contains the light blue square.

![collectandavoid-pathfinding-github](https://user-images.githubusercontent.com/8902454/46189709-c9bf9080-c2a4-11e8-8344-483e46b08c88.png)

Here is an example of a scenario (some details are omitted):
If the AI is currently in the bottom-most subworld, and the light blue square is
in the top-most subworld, the AI will use breadth-first search to move to the
north boundary of its current subworld.  The AI will then move one step north to
enter the new subworld, and then it will again use breadth-first search to move
to the north boundary of this new subworld.  This pattern will continue until
the AI reaches the destination subworld.  Once it reaches the destination
subworld, the AI will use breadth-first search to move toward the light blue
square.
