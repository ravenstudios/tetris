from constants import *
import pygame

import shape
clock = pygame.time.Clock()
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

pygame.init()
shape = shape.Shape(9, 0)
def main():
    running = True

    while running:
        clock.tick(TICK_RATE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw()
        update()

    pygame.quit()



def draw():
    surface.fill((50, 50, 50))#background
    shape.draw(surface)
    pygame.display.flip()



def update():
    pass



if __name__ == "__main__":
    main()
