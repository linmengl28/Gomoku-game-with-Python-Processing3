

class Stone:
    def __init__(self, CELL_SIZE, color):
        self.size = CELL_SIZE*0.9
        self.color = color
        self.ls = []

    def display(self):
        for i in range(len(self.ls)):
            fill(self.color)
            ellipse(self.ls[i][0], self.ls[i][1], self.size, self.size)
