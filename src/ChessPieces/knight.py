import pygame
from src.ChessPieces.chess_piece import ChessPiece

class Knight(ChessPiece):

    def __init__(self, side):
        self.name = "Knight"
        self.side = side

        if side == "black" or "Black":
            self.imagePath = "Sprites/BlackKnight.png"
        else:
            self.imagePath = "Sprites/WhiteKnight.png"



    def move(self):
        print("This is the " + self.side + " " + self.name)