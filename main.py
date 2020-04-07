from constants import *
import pygame

import shape
import playfield

clock = pygame.time.Clock()
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

pygame.init()

shape = shape.Shape(5, 0, O_SHAPE)
playfield = playfield.Playfield()


def main():
    running = True

    while running:
        clock.tick(TICK_RATE)
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_LEFT :
                    shape.move_left()
                if event.key == pygame.K_RIGHT :
                    shape.move_right()
                if event.key == pygame.K_DOWN :
                    shape.fast_drop = True
                if event.key == pygame.K_r :
                    shape.rotate()
                if event.key == pygame.K_q :
                    running = False

            if event.type == pygame.KEYUP :
                if event.key == pygame.K_DOWN :
                    shape.fast_drop = False
            if event.type == pygame.QUIT:
                running = False
        draw()
        update()

    pygame.quit()


def draw():
    surface.fill((200, 200, 200))#background
    playfield.draw(surface)
    shape.draw(surface)
    pygame.display.flip()



def update():
    shape.update(playfield)
    playfield.update()


if __name__ == "__main__":
    main()
