from stone import Stone
from board import Board
from computer import Computer
from game_controller import GameController
from update_score import UpdateScore

cols = 15
rows = 15
WIDTH = 500
HEIGHT = 500
WAIT = 0

new_score = UpdateScore()
board = Board(WIDTH,HEIGHT,cols,rows)
player = Stone(board.CELL_SIZE,0)
pc = Stone(board.CELL_SIZE,1)
gc = GameController(WIDTH,HEIGHT,player,pc,board)
ai = Computer(board,gc)
name_input = False

def setup():
    size(WIDTH, HEIGHT)
    colorMode(RGB, 1)
    

def draw():
    global WAIT,name_input
    background(0.8, 0.6, 0.3)
    if gc.black_wins and not name_input:
        new_score.add_new_score()
        name_input = True
    board.display()
    player.display()
    if WAIT == 0:
        ai.make_move(player,pc)
    else:
        WAIT -= 1
    pc.display()
    gc.update(player,pc)
    


def mousePressed():
    global WAIT
    if gc.is_player_turn:
        gc.play(player,mouseX,mouseY)
        if len(player.ls) - len(pc.ls) == 1:
            WAIT = 50
            gc.player_make_move()
