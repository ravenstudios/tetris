from constants import *
import pygame

import shape
clock = pygame.time.Clock()
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

pygame.init()
shape = shape.Shape(5, 0, T_SHAPE)
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
                    shape.drop()
                if event.key == pygame.K_r :
                    shape.rotate()
                if event.key == pygame.K_q :
                    running = False





            if event.type == pygame.QUIT:
                running = False
        draw()
        update()

    pygame.quit()

def draw_grid():

    for c in range(PLAYFIELD_COLS):
        for r in range(PLAYFIELD_ROWS):
            pygame.draw.rect(surface, BLACK, (PLAYFIELD_OFFSET + c * BLOCK_SIZE, r * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(surface, (150, 150, 150), (PLAYFIELD_OFFSET + c * BLOCK_SIZE + 1, r * BLOCK_SIZE + 1, BLOCK_SIZE - 2, BLOCK_SIZE - 2))

def draw():
    surface.fill((200, 200, 200))#background
    draw_grid()
    shape.draw(surface)
    pygame.display.flip()



def update():
    shape.update()



if __name__ == "__main__":
    main()
