class Banana:
    """A tasty tropical fruit"""
    food_group = 'fruit'
    colors = ['green', 'green-yellow', 'yellow', 'brown spotted', 'black']
    __ripe_colors = ['yellow', 'brown spotted']

    def __init__(self, color='green'):
        if not self.check_color(color):
            raise ValueError(f'A {self.__class__.__name__} cannot be {color}')
        self.color = color
        self.peeled = False

    def _is_ripe(self):
        """Protected method to see if the banana is ripe."""
        return self.color in self.__ripe_colors

    def can_eat(self, must_be_ripe=False):
        """Check if I can eat the banana."""
        if must_be_ripe and not self._is_ripe():
            return False
        return True

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

    def __str__(self):
        # "Magic Attributes" contain metadata about the object
        return f'A {self.color} {self.__class__.__name__}'

class RedBanana(Banana):
    colors = ['green', 'orange', 'red', 'brown', 'black']
    botanical_name = 'red dacca'

    def set_color(self, color):
        if color not in self.colors:
            raise ValueError(f'A Red Banana cannot be {color}!')

    def peel(self):
        super().peel()
        print('It looks like a regular banana inside!') 
