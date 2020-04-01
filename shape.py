import pygame
import block
from constants import *

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        b1 = block.Block(self.x, self.y, RED)
        b2 = block.Block(self.x + 1, self.y, RED)
        b3 = block.Block(self.x, self.y  + 1, RED)
        b4 = block.Block(self.x + 1, self.y  + 1, RED)
        self.blocks = [b1, b2, b3, b4]


    def update(self):
        pass


    def draw(self, surface):
        for b in self.blocks:
            b.draw(surface)
