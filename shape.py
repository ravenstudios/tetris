import pygame
import block
from constants import *

class Shape:
    def __init__(self):

        # self.x = pos[0]
        # self.y = pos[1]
        # self.height = 3
        # self.width = 2
        # b1 = block.Block(self.x, self.y, RED)
        # b2 = block.Block(self.x, self.y + 1, RED)
        # b3 = block.Block(self.x + 1, self.y  + 1, RED)
        # b4 = block.Block(self.x + 1, self.y  + 2, RED)
        # self.blocks = [b1, b2, b3, b4]
        self.drop_rate = 30
        self.rate_counter = 0

    def move_down(self):
        self.rate_counter += 1
        if self.rate_counter % self.drop_rate == 0:
            if self.y + self.height < PLAYFIELD_ROWS:
                self.y += 1
                for b in self.blocks:
                    b.move(0, 1)


    def move_left(self):
            if self.x > 0:
                self.x -= 1
                for b in self.blocks:
                    b.move(-1, 0)



    def move_right(self):
            if self.x + self.width < PLAYFIELD_COLS:
                self.x += 1
                for b in self.blocks:
                    b.move(1, 0)

    def update(self):
        self.move_down()

    def draw(self, surface):
        for b in self.blocks:
            b.draw(surface)
