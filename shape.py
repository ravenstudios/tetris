import pygame
import block
from constants import *
import random

class Shape:
    def __init__(self):

        self.x = 5
        self.y = 1
        self.shapes = [I, T, L, J, Z, S, O]
        self.drop_rate = 30
        self.fast_drop = False
        self.rate_counter = 0
        self.rot_idx = 0
        self.current_shape = self.new_shape()
        self.rotations = self.current_shape["shapes"]
        self.color = self.current_shape["color"]

        b1 = block.Block((self.rotations[0][0][0] + self.x, self.rotations[0][0][1] + self.y), self.color)
        b2 = block.Block((self.rotations[0][1][0] + self.x, self.rotations[0][1][1] + self.y), self.color)
        b3 = block.Block((self.rotations[0][2][0] + self.x, self.rotations[0][2][1] + self.y), self.color)
        b4 = block.Block((self.rotations[0][3][0] + self.x, self.rotations[0][3][1] + self.y), self.color)
        self.blocks = [b1, b2, b3, b4]



    def new_shape(self):
        rdm = random.randint(0, len(self.shapes) - 1)
        return self.shapes[rdm]


    def move_down(self, playfield):
        self.rate_counter += 1
        if self.fast_drop == False:
            #drop slow
            if self.rate_counter % self.drop_rate == 0:
                self.drop(playfield)
        #drop fast
        else:
            self.drop(playfield)



    def drop(self, playfield):
        """
        drops all blocks in a shape down by one row
        """
        bttb = self.blocks_to_bottom(self.rotations[self.rot_idx])

        #if there is a block below any block in the shape we call landed
        if self.block_below(playfield):
            self.landed(playfield)
            return

        #if we hit the bottom we call landed
        if self.y + bttb + 1 >= PLAYFIELD_ROWS:
            self.landed(playfield)
            return

        #if we have not hit the bottom or landed we move down
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




    def update(self, playfield):

        self.move_down(playfield)




    def draw(self, surface):
        for b in self.blocks:
            b.draw(surface)

    def landed(self, playfield):

        self.fast_drop = False
        self.y = 1
        self.x = 5
        for b in self.blocks:
            pos = b.get_pos()
            playfield.add_block(b, pos[0], pos[1])


        self.rot_idx = 0
        self.current_shape = self.new_shape()
        self.rotations = self.current_shape["shapes"]
        self.color = self.current_shape["color"]

        b1 = block.Block((self.rotations[0][0][0] + self.x, self.rotations[0][0][1] + self.y), self.color)
        b2 = block.Block((self.rotations[0][1][0] + self.x, self.rotations[0][1][1] + self.y), self.color)
        b3 = block.Block((self.rotations[0][2][0] + self.x, self.rotations[0][2][1] + self.y), self.color)
        b4 = block.Block((self.rotations[0][3][0] + self.x, self.rotations[0][3][1] + self.y), self.color)
        self.blocks = [b1, b2, b3, b4]





    def block_below(self, playfield):
        pfl = playfield.get_list()

        for b in self.blocks:
            b_pos = b.get_pos()
            if b_pos[1] + 1 < PLAYFIELD_ROWS:
                if pfl[b_pos[0]][b_pos[1] + 1] != 0:
                    return True
        return False

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
