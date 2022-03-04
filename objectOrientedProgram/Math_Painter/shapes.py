class Rectangle:
    def __init__(self, x, y, height, width, color):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color

    def draw(self, canvas):
        """Draws itself into the canvas"""
        # Change a slice of the array with new values
        canvas.data[self.x:self.x + self.height,
                    self.y: self.y+self.width] = self.color


class Square:
    def __init__(self, x, y, side, color):
        self.color = color
        self.x = x
        self.y = y
        self.side = side

    def draw(self, canvas):
        """Draws itself into the canvas"""
        # Change a slice of the array with new values
        canvas.data[self.x:self.x + self.side,
                    self.y: self.y+self.side] = self.color
