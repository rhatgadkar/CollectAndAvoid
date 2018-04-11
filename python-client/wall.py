from stationary_tile import StationaryTile

class Wall(StationaryTile):
    def __init__(self, row, col):
        StationaryTile.__init__(self, row, col)
        self.color = (255, 0, 0)

    def do_something(self):
        pass