import Utils
from Position import Position
from Piece import Piece
from Action import Action

# Clase para le reina

class Queen(Piece):

    def __init__(self, color):
        self.m_color = color

        if (color == 0):
            self.m_type = Utils.wQueen
        else:
            self.m_type = Utils.bQueen

    def getPossibleActions(self, state):

        l = []

        # Movimientos diagonales del alfil
        l = self.getDiagonalUpRightMoves(state)
        l += self.getDiagonalUpLeftMoves(state)
        l += self.getDiagonalDownRightMoves(state)
        l += self.getDiagonalDownLeftMoves(state)

        # Movimientos lineales de la torre
        l += self.getVerticalUpMoves(state)
        l += self.getHorizontalRightMoves(state)
        l += self.getHorizontalLeftMoves(state)
        l += self.getVerticalDownMoves(state)

        
        if self.m_type == Utils.wQueen:
            return l
        else:
            return l.reverse()
        
        