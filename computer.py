import random


class Computer:

    def __init__(self, board, gamecontroller):
        self.board = board
        self.gc = gamecontroller
        self.ready_to_win = False

    def make_move(self, player_stone, pc_stone):
        if self.gc.is_pc_turn:
            defensive_move = self.find_defensive_move(player_stone)
            offensive_move = self.find_offensive_move(pc_stone)

            if self.ready_to_win:
                self.gc.play(pc_stone, offensive_move[0], offensive_move[1])
            elif defensive_move != (None, None):
                self.gc.play(pc_stone, defensive_move[0], defensive_move[1])
            elif offensive_move != (None, None):
                self.gc.play(pc_stone, offensive_move[0], offensive_move[1])
            elif len(self.board.inter_ls) > 0:
                rnd_place = random.choice(list(self.board.inter_ls))
                self.gc.play(pc_stone, rnd_place[0], rnd_place[1])

            self.gc.pc_make_move()

    def find_defensive_move(self, player_stone):
        longest = 1
        (target_x, target_y) = (None, None)
        for (x, y) in self.board.inter_ls:
            player_ls = player_stone.ls + [(x, y)]
            if self.gc.check_longest(player_ls) > longest:
                longest = self.gc.check_longest(player_ls)
                target_x = x
                target_y = y

        return (target_x, target_y)

    def find_offensive_move(self, pc_stone, win=5):
        longest = 1
        (target_x, target_y) = (None, None)
        for (x, y) in self.board.inter_ls:
            pc_ls = pc_stone.ls + [(x, y)]
            if self.gc.check_longest(pc_ls) >= win:
                self.ready_to_win = True
                return (x, y)
            if self.gc.check_longest(pc_ls) > longest:
                longest = self.gc.check_longest(pc_ls)
                target_x = x
                target_y = y

        # print((target_x, target_y))

        return (target_x, target_y)
