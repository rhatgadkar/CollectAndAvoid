class Keys:
    up = True
    down = False
    right = False
    left = False

    @staticmethod
    def set_up():
        Keys.up = True
        Keys.down = False
        Keys.right = False
        Keys.left = False

    @staticmethod
    def set_down():
        Keys.up = False
        Keys.down = True
        Keys.right = False
        Keys.left = False

    @staticmethod
    def set_left():
        Keys.up = False
        Keys.down = False
        Keys.right = False
        Keys.left = True

    @staticmethod
    def set_right():
        Keys.up = False
        Keys.down = False
        Keys.right = True
        Keys.left = False