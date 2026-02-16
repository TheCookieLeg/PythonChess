import pygame
class ChessPiece(pygame.sprite.Sprite):
    name = None
    side = None
    imagePath = None
    currentPosition = pygame.Vector2(0,0)

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

    def move(self):
        raise NotImplementedError("Please implement the move method on this piece")
