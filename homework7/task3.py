"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"
Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"
    [[-, -, o],
     [-, o, o],
     [x, x, x]]
     Return value should be "x wins!"
"""
from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:

    diag1 = [board[i][i] for i in [0, 1, 2]]

    rboard = board[::-1]
    diag2 = [rboard[i][i] for i in [0, 1, 2]]
    if diag1 == ['o', 'o', 'o'] or diag2 == ['o', 'o', 'o']:
        return 'o wins!'
    elif diag1 == ['x', 'x', 'x'] or diag2 == ['x', 'x', 'x']:
        return 'x wins!'
    else:
        for j in range(3):
            colomn = [board[i][j] for i in range(3)]
            print(colomn)
            if colomn == ['o', 'o', 'o']:
                return "o wins!"
            elif colomn == ['x', 'x', 'x']:
                return "x wins!"
            else:
                for line in board:
                    if line == ['o', 'o', 'o']:
                        return 'o wins!'
                    elif line == ['x', 'x', 'x']:
                        return 'x wins!'
    return "unfinished!"
