import random
from params import Params
from circle import Circle

class Trap(Circle):
    def __init__(self):
        x = random.randint(0, Params.SCREEN_WIDTH)
        y = random.randint(0, Params.SCREEN_HEIGHT)
        radius = random.randint(Params.MIN_TRAP_SIZE, Params.MAX_TRAP_SIZE)
        color = Params.TRAP_COLOR
        super().__init__(x, y, radius, color)