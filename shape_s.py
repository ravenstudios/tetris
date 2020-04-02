import pygame
import block
import shape
from constants import *



class Shape_S(shape.Shape):
    def __init__(self, x, y):

        self.x = x
        self.y = y
        self.height = 3
        self.width = 2
        b1 = block.Block(self.x, self.y, RED)
        b2 = block.Block(self.x, self.y + 1, RED)
        b3 = block.Block(self.x + 1, self.y  + 1, RED)
        b4 = block.Block(self.x + 1, self.y  + 2, RED)
        self.blocks = [b1, b2, b3, b4]
        self.drop_rate = 30
        self.rate_counter = 0
