from board import Board


def test_init():
    board = Board(500, 500, 15, 15)
    assert board.CELL_SIZE == 33
    assert len(board.inter_ls) == 225
