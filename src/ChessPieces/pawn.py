from src.ChessPieces.chess_piece import ChessPiece
import pygame


class Pawn(ChessPiece):

    def __init__(self, side):
        ChessPiece.__init__(self)
        self.name = "Pawn"
        self.side = side

        if side == "black" or "Black":
            self.imagePath = "Sprites/BlackPawn.png"
        else:
            self.imagePath = "Sprites/WhitePawn.png"

        self.image = pygame.Surface(self.currentPosition)
        self.image.fill("blue")
        self.rect = (100, 100)


    def move(self):
        print("This is the " + self.side + " " + self.name)