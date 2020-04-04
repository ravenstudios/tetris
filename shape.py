import pygame
import block
from constants import *

class Shape:
    def __init__(self, x, y):

        self.x = x
        self.y = y
        self.width = 0
        self.height = 0

        self.rotations = []
        self.drop_rate = 60
        self.rate_counter = 0
        self.rot_idx = 0

    def move_down(self):
        self.rate_counter += 1
        if self.rate_counter % self.drop_rate == 0:
            if self.y + self.height < PLAYFIELD_ROWS:
                self.y += 1
                for b in self.blocks:
                    b.move((0, 1))


    def move_left(self):
            if self.x > 0:
                self.x -= 1
                for b in self.blocks:
                    b.move((-1, 0))



    def move_right(self):
            if self.x + self.width < PLAYFIELD_COLS:
                self.x += 1
                for b in self.blocks:
                    b.move((1, 0))


    def rotate(self):

        self.rot_idx += 1
        self.rot_idx = self.rot_idx % len(self.rotations)
        i = 0
        for b in self.blocks:

            rot_x = self.rotations[self.rot_idx][i][0] + self.x
            rot_y = self.rotations[self.rot_idx][i][1] + self.y
            b.set_pos((rot_x, rot_y))

            self.width = self.rotations[self.rot_idx][i][0]
            self.height = self.rotations[self.rot_idx][i][1]
            i += 1


    def drop(self):

        while self.y + self.height < PLAYFIELD_ROWS:
            self.y += 1
            for b in self.blocks:
                b.move((0, 1))


    def update(self):
        self.move_down()

    def draw(self, surface):
        for b in self.blocks:
            b.draw(surface)
