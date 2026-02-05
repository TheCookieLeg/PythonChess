import pygame
from src.ChessPieces.chess_piece import ChessPiece
class Queen(ChessPiece):

    def __init__(self, side):
        self.name = "Queen"
        self.side = side

        if side == "black" or "Black":
            self.imagePath = "Sprites/BlackQueen.png"
        else:
            self.imagePath = "Sprites/WhiteQueen.png"



    def move(self):
        print("This is the " + self.side + " " + self.name)