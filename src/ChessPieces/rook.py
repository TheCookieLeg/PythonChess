from src.ChessPieces.chess_piece import ChessPiece
import pygame


class Rook(ChessPiece):

    def __init__(self, side):
        self.name = "Rook"
        self.side = side

        if side == "black" or "Black":
            self.imagePath = "Sprites/BlackRook.png"
        else:
            self.imagePath = "Sprites/WhiteRook.png"





    def move(self):
        print("This is the " + self.side + " " + self.name)