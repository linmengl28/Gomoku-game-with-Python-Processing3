from game_controller import GameController
from stone import Stone
from board import Board


def test_init():
    board = Board(500, 500, 15, 15)
    player = Stone(board.CELL_SIZE, 0)
    pc = Stone(board.CELL_SIZE, 1)
    gc = GameController(500, 500, player, pc, board)

    assert gc.game_tie == False
    assert gc.black_wins == False
    assert gc.white_wins == False
    assert gc.is_player_turn == True
    assert gc.is_pc_turn == False


def test_player_make_move():
    board = Board(500, 500, 15, 15)
    player = Stone(board.CELL_SIZE, 0)
    pc = Stone(board.CELL_SIZE, 1)
    gc = GameController(500, 500, player, pc, board)

    gc.player_make_move()
    assert gc.is_player_turn == False
    assert gc.is_pc_turn == True


def test_pc_make_move():
    board = Board(500, 500, 15, 15)
    player = Stone(board.CELL_SIZE, 0)
    pc = Stone(board.CELL_SIZE, 1)
    gc = GameController(500, 500, player, pc, board)

    gc.pc_make_move()
    assert gc.is_pc_turn == False
    assert gc.is_player_turn == True


def test_play():
    board = Board(500, 500, 15, 15)
    player = Stone(board.CELL_SIZE, 0)
    pc = Stone(board.CELL_SIZE, 1)
    gc = GameController(500, 500, player, pc, board)

    gc.play(player, 52, 52)
    assert (52, 52) not in board.inter_ls
    assert (52, 52) in player.ls


def test_check_longest():
    board = Board(500, 500, 15, 15)
    player = Stone(board.CELL_SIZE, 0)
    pc = Stone(board.CELL_SIZE, 1)
    gc = GameController(500, 500, player, pc, board)

    gc.play(player, 52, 52)
    gc.play(player, 85, 85)
    assert gc.check_longest(player.ls) == 2


def test_check_winner():
    board = Board(500, 500, 15, 15)
    player = Stone(board.CELL_SIZE, 0)
    pc = Stone(board.CELL_SIZE, 1)
    gc = GameController(500, 500, player, pc, board)

    gc.play(player, 52, 52)
    gc.play(player, 85, 85)
    assert gc.check_winner(player) == False
    gc.play(player, 118, 118)
    gc.play(player, 151, 151)
    gc.play(player, 184, 184)
    assert gc.check_winner(player) == True


def test_who_win():
    board = Board(500, 500, 15, 15)
    player = Stone(board.CELL_SIZE, 0)
    pc = Stone(board.CELL_SIZE, 1)
    gc = GameController(500, 500, player, pc, board)

    gc.play(player, 52, 52)
    gc.play(player, 85, 85)
    gc.play(player, 118, 118)
    gc.play(player, 151, 151)
    gc.play(player, 184, 184)
    gc.who_win(player)
    assert gc.black_wins == True
