class Banana:
    """A tasty tropical fruit"""
    food_group = 'fruit'
    colors = ['green', 'green-yellow', 'yellow', 'brown spotted', 'black']

    def __init__(self):
        pass

    def peel(self):
        self.peeled = True

    def set_color(self, color):
        """Set the color of the banana"""
        if color in self.colors:
            self.color = color
        else:
            raise ValueError(f'A banana cannot be {color}!') 

    @classmethod
    def check_color(cls, color):
        """Test a color string to see if it is valid."""
        return color in cls.colors

    @classmethod
    def make_greenie(cls):
        """Create a green banana object"""
        banana = cls()
        banana.set_color('green')
        return banana

    @staticmethod
    def estimate_calories(num_bananas):
        """Given `num_bananas`, estimate the number of calories"""
        return num_bananas * 105
