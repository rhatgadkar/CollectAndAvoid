class Tile(object):
    def __init__(self):
        self.position = (None, None)
        self.color = None

    def do_something(self):
        raise NotImplementedError