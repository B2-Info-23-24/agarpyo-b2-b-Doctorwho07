import random
import pygame
from params import Params
from circle import Circle

class Food(Circle):
    def __init__(self):
        x = random.randint(0, Params.SCREEN_WIDTH)
        y = random.randint(0, Params.SCREEN_HEIGHT)
        radius = Params.FOOD_SIZE
        color = Params.FOOD_COLOR
        super().__init__(x, y, radius, color)