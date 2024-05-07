
class Board:
    def __init__(self, WIDTH, HEIGHT, cols, rows):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.cols = cols - 1
        self.rows = rows - 1
        self.CELL_SIZE = min(self.WIDTH//(self.cols+1),
                             self.HEIGHT//(self.rows+1))
        # LF_BD is the space between left side of back ground and the board
        self.LF_BD = (self.WIDTH - self.cols*self.CELL_SIZE)/2
        self.UP_BD = (self.HEIGHT - self.cols*self.CELL_SIZE)/2
        self.RT_BD = self.WIDTH - self.LF_BD
        self.DN_BD = self.HEIGHT - self.UP_BD

        # inter_ls is the set of coordinates that are available to put a stone
        self.inter_ls = set()
        for i in range(self.cols + 1):
            for j in range(self.rows + 1):
                x = self.LF_BD + self.CELL_SIZE * i
                y = self.UP_BD + self.CELL_SIZE * j
                self.inter_ls.add((x, y))

    def display(self):

        stroke(0)
        strokeWeight(5)

        for i in range(self.cols + 1):
            line(self.LF_BD + self.CELL_SIZE * i, self.UP_BD,
                 self.LF_BD + self.CELL_SIZE * i, self.DN_BD)

        for j in range(self.rows + 1):
            line(self.LF_BD, self.UP_BD + self.CELL_SIZE * j,
                 self.RT_BD, self.UP_BD + self.CELL_SIZE * j)
