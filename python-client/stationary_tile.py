from tile import Tile

class StationaryTile(Tile):
    DIMS = (20, 20)

    def __init__(self, row, col):
        self.row = row
        self.col = col
        x = col * StationaryTile.DIMS[0]
        y = row * StationaryTile.DIMS[1]
        self.position = (x, y)