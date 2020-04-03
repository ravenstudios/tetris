import pygame
import block
import shape
from constants import *



class Shape_T(shape.Shape):
    def __init__(self, x, y):

        self.x = x
        self.y = y

        self.rot_idx = 0 #rotation index
        self.rotations = [
            [(self.x + 1, self.y), (self.x, self.y + 1), (self.x + 1, self.y + 1), (self.x + 2, self.y + 1), (3, 2)],
            [(self.x, self.y), (self.x, self.y + 1), (self.x + 1, self.y + 1), (self.x, self.y + 2), (2, 3)],
            [(self.x, self.y), (self.x + 1, self.y), (self.x + 1, self.y + 1), (self.x + 2, self.y), (3, 2)],
            [(self.x, self.y + 1), (self.x + 1, self.y), (self.x + 1, self.y + 1), (self.x + 1, self.y + 2), (2, 3)]

        ]



        b1 = block.Block(self.rotations[self.rot_idx][0], BLUE)
        b2 = block.Block(self.rotations[self.rot_idx][1], BLUE)
        b3 = block.Block(self.rotations[self.rot_idx][2], BLUE)
        b4 = block.Block(self.rotations[self.rot_idx][3], BLUE)
        self.width = self.rotations[self.rot_idx][4][0]
        self.height = self.rotations[self.rot_idx][4][1]


        self.blocks = [b1, b2, b3, b4]
        self.drop_rate = 10
        self.rate_counter = 0
