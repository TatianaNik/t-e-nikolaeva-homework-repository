from homework7.task3 import tic_tac_toe_checker


def test_tic_tac_toe_checker_x_wins_vertical():
    board1 = [['x', '', 'o'], ['x', 'o', 'o'], ['x', '', '']]
    assert(tic_tac_toe_checker(board1) == "x wins!")


def test_tic_tac_toe_checker_x_wins_horizontal():
    board2 = [['', '', 'o'], ['', 'o', 'o'], ['x', 'x', 'x']]
    assert(tic_tac_toe_checker(board2) == 'x wins!')


def test_tic_tac_toe_checker_o_wins_horizontal():
    board3 = [['', '', 'o'], ['o', 'o', 'o'], ['', 'x', 'x']]
    assert(tic_tac_toe_checker(board3) == 'o wins!')


def test_tic_tac_toe_checker_unfinished():
    board4 = [['', '', 'o'], ['', '', 'o'], ['x', 'x', '']]
    assert(tic_tac_toe_checker(board4) == 'unfinished!')