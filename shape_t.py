import pygame
import block
import shape
from constants import *



class Shape_T(shape.Shape):
    def __init__(self, x, y):
        super().__init__(x, y)



        self.rotations = [
            [(1, 0), (0, 1), (1, 1), (2, 1), (3, 2)],#block 1-4 and (width, height)
            [(0, 0), (0, 1), (1, 1), (0, 2), (2, 3)],
            [(0, 0), (1, 0), (1, 1), (2, 0), (3, 2)],
            [(0, 1), (1, 0), (1, 1), (1, 2), (2, 3)]
        ]


        b1 = block.Block((self.rotations[0][0][0] + self.x, self.rotations[0][0][1] + self.y), BLUE)
        b2 = block.Block((self.rotations[0][1][0] + self.x, self.rotations[0][1][1] + self.y), BLUE)
        b3 = block.Block((self.rotations[0][2][0] + self.x, self.rotations[0][2][1] + self.y), BLUE)
        b4 = block.Block((self.rotations[0][3][0] + self.x, self.rotations[0][3][1] + self.y), BLUE)
        self.width = self.rotations[0][4][0]
        self.height = self.rotations[0][4][1]


        self.blocks = [b1, b2, b3, b4]
    
