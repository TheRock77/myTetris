import pygame, random

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Auflösung des Spiels
TILESIZE = 30
COLUMS = 13
ROWS = 22
SCREEN_WIDTH = TILESIZE * COLUMS
SCREEN_HEIGHT = TILESIZE * ROWS

# Spielfeldfarben
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
BLACK = (0, 0, 0)

# TILE Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
TURQUOISE = (0, 255, 255)
PINK = (255, 0, 255)

COLORS = [RED, GREEN, BLUE, YELLOW, ORANGE, TURQUOISE, PINK]

BOARD = [[BLACK for i in range(COLUMS)] for j in range(ROWS)]

I = [[
    [1, 0, 0, 0],
    [1, 0, 0, 0],
    [1, 0, 0, 0],
    [1, 0, 0, 0]],
    [
        [1, 1, 1, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]]

O = [[
    [1, 1, 0, 0],
    [1, 1, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]]

T = [[
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]],
    [
        [0, 1, 0, 0],
        [1, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0]],
    [
        [0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]],
    [
        [1, 0, 0, 0],
        [1, 1, 0, 0],
        [1, 0, 0, 0],
        [0, 0, 0, 0]]
]

L = [[
    [1, 0, 0, 0],
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 0, 0, 0]],
    [
        [1, 1, 1, 0],
        [1, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]],
    [
        [1, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0]],
    [
        [0, 0, 1, 0],
        [1, 1, 1, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]
]

J = [[
    [0, 1, 0, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0],
    [0, 0, 0, 0]],
    [
        [1, 0, 0, 0],
        [1, 1, 1, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]],
    [
        [1, 1, 0, 0],
        [1, 0, 0, 0],
        [1, 0, 0, 0],
        [0, 0, 0, 0]],
    [
        [1, 1, 1, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]
]

S = [[
    [0, 1, 1, 0],
    [1, 1, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]],
    [
        [1, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0]]
]

Z = [[
    [1, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]],
    [
        [0, 1, 0, 0],
        [1, 1, 0, 0],
        [1, 0, 0, 0],
        [0, 0, 0, 0]]
]

SHAPES = [I, O, T, L, J, S, Z]

pygame.init()
pygame.display.set_caption('Boni\'s Tetris')

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
clock = pygame.time.Clock()


class Tile():
    def __init__(self, shape, x=5, y=1, rotation=0, color=0):
        self.x = x
        self.y = y
        self.shape = shape
        self.rotation = rotation
        self.color = color
        self.right = 2
        self.bottom = 1

    def update(self, pressedKey=None):
        if pressedKey is None:
            if not checkCollision(self.x, self.y + 1, self.shape):
                self.y += 1
        elif pressedKey[K_RIGHT]:
            if not checkCollision(self.x + 1, self.y, self.shape):
                self.x += 1
        elif pressedKey[K_LEFT]:
            if not checkCollision(self.x - 1, self.y, self.shape):
                self.x -= 1
        elif pressedKey[K_DOWN]:
            if not checkCollision(self.x, self.y + 1, self.shape):
                self.y += 1
        elif pressedKey[K_UP]:
            self.rotation = (self.rotation + 1) % len(self.shape)


"""
        if self.x < 1:
            self.x = 1
        if self.x > 11 - self.right:
            self.x = 11 - self.right
        if self.y > 20 - self.bottom:
            self.y = 20 - self.bottom
"""


def initBoard():
    for i in range(ROWS):
        for j in range(COLUMS):
            if (i == 0 or i == ROWS - 1):
                BOARD[i][j] = GREY

            elif (j == 0 or j == COLUMS - 1):
                BOARD[i][j] = GREY

            else:
                BOARD[i][j] = BLACK


def checkCollision(x, y, shape):
    print(y, x)
    print(BOARD[y][x])
    if BOARD[y][x] != BLACK:
        print(BOARD[y][x])
        for i in range(4):
            for j in range(4):
                print("Tile: ", shape[i][j])
                if shape[0][i][j] == 1:
                    print("True")
                    return True
    return False


def drawBorders():
    for x in range(0, SCREEN_WIDTH, 30):
        pygame.draw.rect(screen, GREY, (x + 2, 2, (TILESIZE - 2), (TILESIZE - 2)))
        pygame.draw.rect(screen, GREY, (x + 2, SCREEN_HEIGHT - TILESIZE + 2, (TILESIZE - 2), (TILESIZE - 2)))

    for y in range(30, SCREEN_HEIGHT - 30, 30):
        pygame.draw.rect(screen, GREY, (2, y + 2, (TILESIZE - 2), (TILESIZE - 2)))
        pygame.draw.rect(screen, GREY, (SCREEN_WIDTH - TILESIZE + 2, y + 2, (TILESIZE - 2), (TILESIZE - 2)))


def main():
    MOVEDOWNTILE = pygame.USEREVENT + 1
    pygame.time.set_timer(MOVEDOWNTILE, 1000)

    initBoard()

    running = True

    currentTile = Tile(shape=SHAPES[random.randint(0, 6)], color=COLORS[random.randint(0, 6)])
    nextTile = Tile(shape=SHAPES[random.randint(0, 6)], color=COLORS[random.randint(0, 6)])

    while running:

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == pygame.QUIT:
                running = False
            elif event.type == MOVEDOWNTILE:
                currentTile.update()

            pressedKey = pygame.key.get_pressed()
            currentTile.update(pressedKey)

        if checkCollision(currentTile.x, currentTile.y, currentTile.shape):
            currentTile = nextTile
            nextTile = Tile(shape=SHAPES[random.randint(0, 6)], color=COLORS[random.randint(0, 6)])

        screen.fill(BLACK)
        drawBorders()

        for i in range(4):
            for j in range(4):
                if currentTile.shape[currentTile.rotation][i][j] == 1:
                    pygame.draw.rect(screen, currentTile.color, ((currentTile.x + j) * TILESIZE + 1, (currentTile.y + i)
                                                                 * TILESIZE + 1, TILESIZE - 1, TILESIZE - 1))

        pygame.display.flip()

        clock.tick(30)


if __name__ == '__main__':
    main()
