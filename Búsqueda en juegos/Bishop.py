import Utils
from Position import Position
from Piece import Piece
from Action import Action

# Clase para el Alfil

class Bishop(Piece):

    def __init__(self, color):
        self.m_color = color

        if (color == 0):
            self.m_type = Utils.wBishop
        else:
            self.m_type = Utils.bBishop

    def getPossibleActions(self, state):

        l = []
        

        l = self.getDiagonalUpRightMoves(state)
        l += self.getDiagonalUpLeftMoves(state)
        l += self.getDiagonalDownRightMoves(state)
        l += self.getDiagonalDownLeftMoves(state)

        if self.m_type == Utils.wBishop:
            return l
        else:
            return l.reverse()