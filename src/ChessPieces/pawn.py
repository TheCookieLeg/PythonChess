from src.ChessPieces.chess_piece import ChessPiece
import pygame


class Pawn(ChessPiece):

    def __init__(self, side):
        self.name = "Pawn"
        self.side = side

        if side == "black" or "Black":
            self.imagePath = "Sprites/BlackPawn.png"
        else:
            self.imagePath = "Sprites/WhitePawn.png"



    def move(self):
        print("This is the " + self.side + " " + self.name)