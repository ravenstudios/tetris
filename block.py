import pygame
from constants import *

class Block:
    def __init__(self, r, c, color):
        self.width = BLOCK_SIZE
        self.height = BLOCK_SIZE
        self.r = r
        self.c = c
        self.x = r * BLOCK_SIZE
        self.y = c  * BLOCK_SIZE
        self.color = color


    def update(self):
        pass


    def draw(self, surface):
        pygame.draw.rect(surface, BLACK, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(surface, self.color, (self.x + 4, self.y + 4, self.width - 8, self.height - 8))



    def set_pos(self, pos):
        self.r = pos.r
        slef.c = pos.c


    def get_pos(self):
        return {"r":slef.r, "c":self.c, "width":self.width, "height": self.height}
