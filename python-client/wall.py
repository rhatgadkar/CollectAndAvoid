from tile import Tile

class Wall(Tile):
    def __init__(self, row, col):
        self.row = row
        self.col = col
        x = col * Tile.DIMS[0]
        y = row * Tile.DIMS[1]
        self.position = (x, y)
        self.color = (255, 0, 0)

    def do_something(self):
        pass