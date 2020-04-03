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
        pygame.draw.rect(surface, self.color, (self.x + 4, self.y + 4, self.width - 8, self.height - 8))



    def move(self, r, c):
        self.r += r
        self.c += c


    def get_pos(self):
        return {"r":slef.r, "c":self.c, "width":self.width, "height": self.height}
