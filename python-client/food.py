from stationary_tile import StationaryTile

class Food(StationaryTile):
    def __init__(self, row, col):
        StationaryTile.__init__(self, row, col)
        self.color = (0, 255, 255)

    def do_something(self):
        pass