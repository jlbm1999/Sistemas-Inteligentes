import Utils
from Position import Position
from Piece import Piece
from Action import Action

# Clase para el rey

class King(Piece):

    def __init__(self, color):
        self.m_color = color

        if (color == 0):
            self.m_type = Utils.wKing
        else:
            self.m_type = Utils.bKing
    
    
    def getPossibleActions(self, state):

        r = state.m_agentPos.row
        c = state.m_agentPos.col
        oponent_color = -1
        l = []

        if (self.m_color == 0):  # White King
            oponent_color = 1
        else:                   # Black King
            oponent_color = 0

        # Para cada movimiento, lo primero que comprobamos es que esa casilla esté dentro del tablero. Después, nos aseguramos de que está vacía.
        # En la segunda parte de la OR, comprobamos que estamos en los límites, y que la ficha que ocupa la casilla es del color del oponente para poder comérnosla
        
        if ((r > 0 and state.m_board[r-1][c] == Utils.empty) 
            or (r > 0 and  state.m_board[r-1][c] != Utils.empty and Utils.getColorPiece(state.m_board[r-1][c]) == oponent_color)): 
            l.append(Action(state.m_agentPos, Position(r-1,c)))                 # Movimiento hacia arriba
        
        if ((c < state.m_boardSize-1 and state.m_board[r][c+1] == Utils.empty) 
            or (c < state.m_boardSize-1 and state.m_board[r][c+1] != Utils.empty and Utils.getColorPiece(state.m_board[r][c+1]) == oponent_color)):
            l.append(Action(state.m_agentPos, Position(r,c+1)))                 # Movimiento hacia drcha
        
        if ((c > 0 and state.m_board[r][c-1] == Utils.empty) 
            or (c > 0 and state.m_board[r][c-1] != Utils.empty and Utils.getColorPiece(state.m_board[r][c-1]) == oponent_color)):      
            l.append(Action(state.m_agentPos, Position(r,c-1)))                 # Movimiento hacia izqda
        
        if ((r < state.m_boardSize-1 and state.m_board[r+1][c] == Utils.empty) 
            or (r < state.m_boardSize-1 and state.m_board[r+1][c] != Utils.empty and Utils.getColorPiece(state.m_board[r+1][c]) == oponent_color)):
            l.append(Action(state.m_agentPos, Position(r+1,c)))                 # Movimiento hacia abajo


			
        if ((r > 0 and c > 0 and state.m_board[r-1][c-1] == Utils.empty) 
            or (r > 0 and c > 0 and state.m_board[r-1][c-1] != Utils.empty and Utils.getColorPiece(state.m_board[r-1][c-1]) == oponent_color)):     
            l.append(Action(state.m_agentPos, Position(r-1,c-1)))               # Diagonal arriba izqda
			
        if ((r > 0 and c < state.m_boardSize-1 and state.m_board[r-1][c+1] == Utils.empty) 
            or (r > 0 and c < state.m_boardSize-1 and state.m_board[r-1][c+1] != Utils.empty and Utils.getColorPiece(state.m_board[r-1][c+1]) == oponent_color)): 
            l.append(Action(state.m_agentPos, Position(r-1,c+1)))               # Diagonal arriba derecha
        
        if ((r < state.m_boardSize-1 and c < state.m_boardSize-1 and state.m_board[r+1][c+1] == Utils.empty) 
            or (r < state.m_boardSize-1 and c < state.m_boardSize-1 and state.m_board[r+1][c+1] != Utils.empty and Utils.getColorPiece(state.m_board[r+1][c+1]) == oponent_color)): 
            l.append(Action(state.m_agentPos, Position(r+1,c+1)))               # Diagonal abajo derecha
        
        if ((r < state.m_boardSize-1 and c > 0 and state.m_board[r+1][c-1] == Utils.empty) 
            or (r < state.m_boardSize-1 and c > 0 and state.m_board[r+1][c-1] != Utils.empty and Utils.getColorPiece(state.m_board[r+1][c-1]) == oponent_color)):    
            l.append(Action(state.m_agentPos, Position(r+1,c-1)))               # Diagonal abajo izqda

			
        return l
        
        
