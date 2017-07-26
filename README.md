Build a Game-playing Agent
===========================


In this project, I will develop an adversarial search agent to play the game "Isolation".  Isolation is a deterministic, two-player game of perfect information in which the players alternate turns moving a single piece from one cell to another on a board.  Whenever either player occupies a cell, that cell becomes blocked for the remainder of the game.  The first player with no remaining legal moves loses, and the opponent is declared the winner.

![Example game of isolation](aind/viz.gif)

This project uses a version of Isolation where each agent is restricted to L-shaped movements (like a knight in chess) on a rectangular grid (like a chess or checkerboard).  The agents can move to any open cell on the board that is 2-rows and 1-column or 2-columns and 1-row away from their current position on the board. Movements are blocked at the edges of the board (the board does not wrap around), however, the player can "jump" blocked or occupied spaces (just like a knight in chess).

Additionally, agents will have a fixed time limit each turn to search for the best move and respond.  If the time limit expires during a player's turn, that player forfeits the match, and the opponent wins. This project is part of the [Artificial Intelligence Nanodegree](https://www.udacity.com/course/artificial-intelligence-nanodegree--nd889) program, from Udacity. You can check my report <a href="" target="_blank">here</a>


### Install
This project requires **Python 3** and the following Python libraries installed:
- [NumPy](http://www.numpy.org/)
- [Unittest](https://docs.python.org/2/library/unittest.html)


### Run
In a terminal or command window, navigate to the top-level project directory `Isolation/` (that contains this README) and run the following command:

```shell
$ python -m aind.sample_players
```

### Main References
1. RUSSELL, S.; NORVING, P. *Artificial Intelligence: A Modern Approach*. 3rd ed. Prentice Hall Press, 2009.
2. Udacity original code. [link](https://github.com/udacity/AIND-Isolation)


### License
The contents of this repository are covered under the [MIT License](LICENSE.md).
