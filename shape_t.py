import pygame
import block
import shape
from constants import *



class Shape_T(shape.Shape):
    def __init__(self, x, y):

        self.x = x
        self.y = y
        self.height = 2
        self.width = 3
        b1 = block.Block(self.x + 1, self.y, BLUE)
        b2 = block.Block(self.x, self.y + 1, BLUE)
        b3 = block.Block(self.x + 1, self.y + 1, BLUE)
        b4 = block.Block(self.x + 2, self.y + 1, BLUE)
        self.blocks = [b1, b2, b3, b4]
        self.drop_rate = 30
        self.rate_counter = 0
