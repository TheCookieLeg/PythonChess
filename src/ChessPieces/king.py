import pygame
from src.ChessPieces.chess_piece import ChessPiece
class King(ChessPiece):

    def __init__(self, side):
        self.name = "King"
        self.side = side

        if side == "black" or "Black":
            self.imagePath = "Sprites/BlackKing.png"
        else:
            self.imagePath = "Sprites/WhiteKing.png"



    def move(self):
        print("This is the " + self.side + " " + self.name)