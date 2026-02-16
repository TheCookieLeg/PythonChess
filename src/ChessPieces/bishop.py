import pygame
from src.ChessPieces.chess_piece import ChessPiece
class Bishop(ChessPiece):

    def __init__(self, side):
        ChessPiece.__init__(self)
        self.name = "Bishop"
        self.side = side

        if side == "black" or "Black":
            self.imagePath = "Sprites/BlackBishop.png"
        else:
            self.imagePath = "Sprites/WhiteBishop.png"



    def move(self):
        print("This is the " + self.side + " " + self.name)