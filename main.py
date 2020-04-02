from constants import *
import pygame

import shape_t
clock = pygame.time.Clock()
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

pygame.init()
shape_t = shape_t.Shape_T(5, 0)
def main():
    running = True

    while running:
        clock.tick(TICK_RATE)
        for event in pygame.event.get():
            if event.type == pygame.KEYUP :
                if event.key == pygame.K_LEFT :
                    shape_t.move_left()
                if event.key == pygame.K_RIGHT :
                    shape_t.move_right()
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
    shape_t.draw(surface)
    pygame.display.flip()



def update():
    shape_t.update()



if __name__ == "__main__":
    main()
