import pygame
import block
from constants import *

class Shape:
    def __init__(self, x, y, rots):

        self.x = x
        self.y = y
        # self.width = 0
        # self.height = 0


        self.drop_rate = 60
        self.rate_counter = 0
        self.rot_idx = 0

        self.rotations = rots

        b1 = block.Block((self.rotations[0][0][0] + self.x, self.rotations[0][0][1] + self.y), BLUE)
        b2 = block.Block((self.rotations[0][1][0] + self.x, self.rotations[0][1][1] + self.y), BLUE)
        b3 = block.Block((self.rotations[0][2][0] + self.x, self.rotations[0][2][1] + self.y), BLUE)
        b4 = block.Block((self.rotations[0][3][0] + self.x, self.rotations[0][3][1] + self.y), BLUE)
        # self.width = self.rotations[0][4][0]
        # self.height = self.rotations[0][4][1]
        self.blocks = [b1, b2, b3, b4]

    def move_down(self):
        self.rate_counter += 1
        if self.rate_counter % self.drop_rate == 0:
            bttb = self.blocks_to_bottom(self.rotations[self.rot_idx])
            if self.y + bttb + 1 < PLAYFIELD_ROWS:#the + 1 accounts for the height of the block
                self.y += 1
                for b in self.blocks:
                    b.move((0, 1))

    def move_left(self):
        bttl = self.blocks_to_left(self.rotations[self.rot_idx])

        if self.x - bttl > 0:
            self.x -= 1
            for b in self.blocks:
                b.move((-1, 0))

    def move_right(self):
        bttr = self.blocks_to_right(self.rotations[self.rot_idx])
        if self.x + bttr + 1< PLAYFIELD_COLS:#the + 1 accounts for the width of the block
            self.x += 1
            for b in self.blocks:
                b.move((1, 0))

    def rotate(self):


        self.rot_idx += 1

        self.rot_idx = self.rot_idx % len(self.rotations)

        bttl = self.blocks_to_left(self.rotations[self.rot_idx])
        bttr = self.blocks_to_right(self.rotations[self.rot_idx])

        if self.x - bttl < 0:
            self.x += bttl

        if self.x + bttr + 1 > PLAYFIELD_COLS:
            self.x -= bttr
        i = 0
        for b in self.blocks:

            rot_x = self.rotations[self.rot_idx][i][0] + self.x
            rot_y = self.rotations[self.rot_idx][i][1] + self.y
            b.set_pos((rot_x, rot_y))

            i += 1

    def drop(self):

        bttb = self.blocks_to_bottom(self.rotations[self.rot_idx])
        while self.y + bttb + 1 < PLAYFIELD_ROWS:#the + 1 accounts for the height of the block
            self.y += 1
            for b in self.blocks:
                b.move((0, 1))

    def update(self):
        self.move_down()

    def draw(self, surface):
        for b in self.blocks:
            b.draw(surface)

    def landed(self):
        pass

    def blocks_to_left(self, list):
        lowest_x = 0

        for l in list:
            if l[0] < lowest_x:
                lowest_x = l[0]

        return -lowest_x #needs to be inverted

    def blocks_to_right(self, list):
        highest_x = 0

        for l in list:
            if l[0] > highest_x:
                highest_x = l[0]

        return highest_x

    def blocks_to_bottom(self, list):
        highest_y = 0

        for l in list:
            if l[1] > highest_y:
                highest_y = l[1]

        return highest_y
