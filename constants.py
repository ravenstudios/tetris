GAME_WIDTH = 800
GAME_HEIGHT = 600
BLOCK_SIZE = 24
PLAYFIELD_COLS = 10
PLAYFIELD_ROWS = 22
PLAYFIELD_OFFSET = GAME_WIDTH // 2 - PLAYFIELD_COLS * BLOCK_SIZE // 2
TICK_RATE = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


T_SHAPE = [
    [(0, -1), (-1, 0), (0, 0), (1, 0)],#block 1-4 and (width, height)
    [(0, -1), (0, 0), (1, 0), (0, 1)],
    [(0, 1), (-1, 0), (0, 0), (1, 0)],
    [(0, -1), (0, 0), (-1, 0), (0, 1)]
]
