from operator import truediv

import pygame


def currentTileColor(c):
    if (c % 2 == 0):
        return "white"
    return "brown"

def drawChessBoard():
    col = 0
    row = 0
    counter = 0
    for i in range(8):
        for j in range(8):
            pygame.draw.rect(screen, currentTileColor(counter), (col, row, TILE_SIZE, TILE_SIZE))
            row += TILE_SIZE
            counter += 1
        row = 0
        col += TILE_SIZE
        counter += 1


TILE_SIZE = 100

pygame.init()
screen = pygame.display.set_mode((TILE_SIZE * 8, TILE_SIZE * 8))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    drawChessBoard()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

