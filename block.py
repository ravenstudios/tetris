import pygame
from constants import *

class Block:
    def __init__(self, pos, color):
        self.width = BLOCK_SIZE
        self.height = BLOCK_SIZE
        self.r = pos[0]
        self.c = pos[1]
        self.x = self.r * BLOCK_SIZE + PLAYFIELD_OFFSET
        self.y = self.c  * BLOCK_SIZE
        self.color = color


    def update(self):
        pass


    def draw(self, surface):
        #updates the x and y from row and col
        self.x = self.r * BLOCK_SIZE + PLAYFIELD_OFFSET
        self.y = self.c  * BLOCK_SIZE

        pygame.draw.rect(surface, BLACK, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(surface, self.color, (self.x + 2, self.y + 2, self.width - 4, self.height - 4))



    def move(self, pos):
        self.r += pos[0]
        self.c += pos[1]

    def set_pos(self, pos):
        self.r = pos[0]
        self.c = pos[1]

    def get_pos(self):
        return (self.r, self.c)
