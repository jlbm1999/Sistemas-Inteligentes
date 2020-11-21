import Utils
from Position import Position
from Piece import Piece
from Action import Action

# Clase para el caballo

class Knight(Piece):

    def __init__(self, color):
        self.m_color = color

        if (color == 0):
            self.m_type = Utils.wKnight
        else:
            self.m_type = Utils.bKnight
    
    def getPossibleActions(self, state):

        r = state.m_agentPos.row
        c = state.m_agentPos.col
        oponent_color = -1
        l = []

        if (self.m_color == 0):  # White Knight
            oponent_color = 1
        else:                   # Black Knight
            oponent_color = 0

        
        if((r > 1 and c < state.m_boardSize-1 and state.m_board[r-2][c+1] == Utils.empty) 
			or (r > 1 and c < state.m_boardSize-1 and state.m_board[r-2][c+1] != Utils.empty and Utils.getColorPiece(state.m_board[r-2][c+1]) == oponent_color)):
            l.append(Action(state.m_agentPos, Position(r-2,c+1)))
        
        if((r > 1 and c > 0 and state.m_board[r-2][c-1] == Utils.empty) 
			or (r > 1 and c > 0 and state.m_board[r-2][c-1] != Utils.empty and Utils.getColorPiece(state.m_board[r-2][c-1]) == oponent_color)):
            l.append(Action(state.m_agentPos, Position(r-2,c-1)))

        if((r > 0 and c > 1 and state.m_board[r-1][c-2] == Utils.empty) 
			or (r > 0 and c > 1 and state.m_board[r-1][c-2] != Utils.empty and Utils.getColorPiece(state.m_board[r-1][c-2]) == oponent_color)):
            l.append(Action(state.m_agentPos, Position(r-1,c-2)))
        
        if((r > 0 and c < state.m_boardSize-2 and state.m_board[r-1][c+2] == Utils.empty) 
			or (r > 0 and c < state.m_boardSize-2 and state.m_board[r-1][c+2] != Utils.empty and Utils.getColorPiece(state.m_board[r-1][c+2]) == oponent_color)):
            l.append(Action(state.m_agentPos, Position(r-1,c+2)))
        
        if((r < state.m_boardSize-1 and c > 1 and state.m_board[r+1][c-2] == Utils.empty) 
			or (r < state.m_boardSize-1 and c > 1 and state.m_board[r+1][c-2] != Utils.empty and Utils.getColorPiece(state.m_board[r+1][c-2]) == oponent_color)):
            l.append(Action(state.m_agentPos, Position(r+1,c-2)))
        
        if((r > state.m_boardSize-1 and c < state.m_boardSize-2 and state.m_board[r+1][c+2] == Utils.empty) 
			or (r > state.m_boardSize-1 and c < state.m_boardSize-2 and state.m_board[r+1][c+2] != Utils.empty and Utils.getColorPiece(state.m_board[r+1][c+2]) == oponent_color)):
            l.append(Action(state.m_agentPos, Position(r+1,c+2)))
        
        if((r < state.m_boardSize-2 and c < state.m_boardSize-1 and state.m_board[r+2][c+1] == Utils.empty) 
			or (r < state.m_boardSize-2 and c < state.m_boardSize-1 and state.m_board[r+2][c+1] != Utils.empty and Utils.getColorPiece(state.m_board[r+2][c+1]) == oponent_color)):
            l.append(Action(state.m_agentPos, Position(r+2,c+1)))

        if((r < state.m_boardSize-2 and c > 0 and state.m_board[r+2][c-1] == Utils.empty) 
			or (r < state.m_boardSize-2 and c > 0 and state.m_board[r+2][c-1] != Utils.empty and Utils.getColorPiece(state.m_board[r+2][c-1]) == oponent_color)):
            l.append(Action(state.m_agentPos, Position(r+2,c-1)))
        

        return l        

