from operator import truediv

import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.rect(screen, "white", (pos.x, pos.y, 100, 100), 10)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()