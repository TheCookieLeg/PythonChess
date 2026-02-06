import pygame
class ChessPiece(pygame.sprite.Sprite):
    name = None
    side = None
    imagePath = None
    pygame.Vector2(0,0)


    def move(self):
        raise NotImplementedError("Please implement the move method on this piece")
