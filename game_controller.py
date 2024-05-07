import random


class GameController:
    def __init__(self, WIDTH, HEIGHT, player_stone, pc_stone, board):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.player_st = player_stone
        self.pc_st = pc_stone
        self.board = board
        self.game_tie = False
        self.black_wins = False
        self.white_wins = False
        self.is_player_turn = True
        self.is_pc_turn = False

    def update(self, player_st, pc_st):
        self.who_win(player_st)
        self.who_win(pc_st)
        if self.game_tie:
            fill(0, 1, 1)
            textSize(self.WIDTH*0.1)
            textAlign(CENTER, CENTER)
            text("GAME OVER", self.WIDTH/2, self.HEIGHT/2)

        if self.black_wins:
            fill(0, 1, 1)
            textSize(self.WIDTH*0.1)
            textAlign(CENTER, CENTER)
            text("BLACK WINS", self.WIDTH/2, self.HEIGHT/2)

        if self.white_wins:
            fill(0, 1, 1)
            textSize(self.WIDTH*0.1)
            textAlign(CENTER, CENTER)
            text("WHITE WINS", self.WIDTH/2, self.HEIGHT/2)

    def player_make_move(self):
        self.is_player_turn = False
        self.is_pc_turn = True

    def pc_make_move(self):
        self.is_player_turn = True
        self.is_pc_turn = False

    def who_win(self, stone):
        win = 5
        if len(stone.ls) >= win and self.check_winner(stone):
            self.is_pc_turn = False
            self.is_player_turn = False
            if stone.color == 0:
                self.black_wins = True
            elif stone.color == 1:
                self.white_wins = True
        elif len(self.board.inter_ls) == 0:
            self.game_tie = True
            self.is_pc_turn = False
            self.is_player_turn = False

    def check_winner(self, stone):
        win = 5
        return self.check_longest(stone.ls) >= win

    def check_longest(self, ls):
        longest_ls = []
        if len(ls) > 0:
            last = ls[-1]
            # check horizontally, vertically, diagonally(2 directions)
            for direction in {(1, 0), (0, 1), (1, 1), (1, -1)}:
                count = 1
                # check 2 different directions
                for inverse in [1, -1]:
                    dx = direction[0]*inverse*self.board.CELL_SIZE
                    dy = direction[1]*inverse*self.board.CELL_SIZE
                    x = last[0] + dx
                    y = last[1] + dy
                    while (x, y) in ls:
                        count += 1
                        x += dx
                        y += dy
                longest_ls.append(count)

        if longest_ls:
            return max(longest_ls)
        else:
            return 0

    def play(self, stone, x, y):
        # find the nearest legal coordinate
        remainder_x = (x-self.board.LF_BD) % self.board.CELL_SIZE
        remainder_y = (y-self.board.UP_BD) % self.board.CELL_SIZE
        if remainder_x > self.board.CELL_SIZE/2:
            place_x = x + self.board.CELL_SIZE - remainder_x
        else:
            place_x = x - remainder_x

        if remainder_y > self.board.CELL_SIZE/2:
            place_y = y + self.board.CELL_SIZE - remainder_y
        else:
            place_y = y - remainder_y

        if (place_x, place_y) in self.board.inter_ls:
            stone.ls.append((place_x, place_y))
            self.board.inter_ls.remove((place_x, place_y))
