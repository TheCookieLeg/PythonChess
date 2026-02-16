import pygame

from src.ChessPieces.chess_piece import ChessPiece
from src.ChessPieces.rook import Rook
from src.ChessPieces.knight import Knight
from src.ChessPieces.bishop import Bishop
from src.ChessPieces.queen import Queen
from src.ChessPieces.king import King
from src.ChessPieces.pawn import Pawn

def initPieces(side):
    arr = [#Rook(side), Rook(side),
           #Knight(side), Knight(side),
           #Bishop(side), Bishop(side),
           #Queen(side), King(side),
           Pawn(side), Pawn(side), Pawn(side), Pawn(side),
           Pawn(side), Pawn(side), Pawn(side), Pawn(side)]
    return arr

def addPiecesToGroup(pieceArr):
    group = pygame.sprite.Group()
    for piece in pieceArr:
        group.add(piece)
    return group
