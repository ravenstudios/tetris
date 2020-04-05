from constants import *
import pygame
import block

class Playfield:

    def __init__(self):
        self.blocks = []

        for c in range(PLAYFIELD_COLS):
            row = []
            for r in range(PLAYFIELD_ROWS):
                row.append(0)
            self.blocks.append(row)


    def add_block(self, block, c, r):
        self.blocks[c][r] = block

    def get_list(self):
        return self.blocks
    def update(self):
        pass


    def draw(self, surface):
        for c in range(PLAYFIELD_COLS):
            for r in range(PLAYFIELD_ROWS):
                pygame.draw.rect(surface, BLACK, (PLAYFIELD_OFFSET + c * BLOCK_SIZE, r * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                pygame.draw.rect(surface, (150, 150, 150), (PLAYFIELD_OFFSET + c * BLOCK_SIZE + 1, r * BLOCK_SIZE + 1, BLOCK_SIZE - 2, BLOCK_SIZE - 2))

        for c in range(PLAYFIELD_COLS):
            for r in range(PLAYFIELD_ROWS):
                if self.blocks[c][r] != 0:
                    self.blocks[c][r].draw(surface)
