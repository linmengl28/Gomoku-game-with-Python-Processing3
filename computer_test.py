from computer import Computer
from board import Board
from game_controller import GameController
from stone import Stone


def test_init():
    board = Board(500, 500, 15, 15)
    player = Stone(board.CELL_SIZE, 0)
    pc = Stone(board.CELL_SIZE, 1)
    gc = GameController(500, 500, player, pc, board)
    ai = Computer(board, gc)
    assert ai.ready_to_win == False


def test_find_offensive_move():
    board = Board(500, 500, 15, 15)
    player = Stone(board.CELL_SIZE, 0)
    pc = Stone(board.CELL_SIZE, 1)
    gc = GameController(500, 500, player, pc, board)
    ai = Computer(board, gc)
    gc.play(player, 19, 19)
    gc.play(pc, 52, 52)
    gc.play(pc, 85, 85)
    gc.play(pc, 118, 118)
    assert ai.find_offensive_move(pc) == (151, 151)
    gc.play(pc, 151, 151)
    assert ai.find_offensive_move(pc) == (184, 184)


def test_find_defensive_move():
    board = Board(500, 500, 15, 15)
    player = Stone(board.CELL_SIZE, 0)
    pc = Stone(board.CELL_SIZE, 1)
    gc = GameController(500, 500, player, pc, board)
    ai = Computer(board, gc)
    gc.play(pc, 19, 19)
    gc.play(player, 52, 52)
    gc.play(player, 85, 85)
    gc.play(player, 118, 118)
    assert ai.find_defensive_move(player) == (151, 151)


def test_make_move():
    board = Board(500, 500, 15, 15)
    player = Stone(board.CELL_SIZE, 0)
    pc = Stone(board.CELL_SIZE, 1)
    gc = GameController(500, 500, player, pc, board)
    ai = Computer(board, gc)

    # test random move
    gc.is_pc_turn = True
    ai.make_move(player, pc)
    assert len(player.ls) - len(pc.ls) == -1

    # test offensive move
    gc.play(pc, 19, 19)
    gc.play(pc, 19, 52)
    gc.is_pc_turn = True
    ai.make_move(player, pc)
    assert (19, 85) in pc.ls

    # test defensive move
    gc.play(player, 52, 52)
    gc.play(player, 85, 85)
    gc.play(player, 118, 118)
    gc.is_pc_turn = True
    ai.make_move(player, pc)
    assert (151, 151) in pc.ls

    # test offensive move_ ready to win
    gc.play(pc, 52, 19)
    gc.play(pc, 85, 19)
    gc.play(pc, 118, 19)
    gc.is_pc_turn = True
    ai.make_move(player, pc)
    assert (151, 19) in pc.ls
