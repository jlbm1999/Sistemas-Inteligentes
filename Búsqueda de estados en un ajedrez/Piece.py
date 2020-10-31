#import java.util.ArrayList;

# this class implements the getPossibleActions for each type of piece

import Utils
from Position import Position
from Action import Action
from State import State

class Piece:
	# this method must be completed with all the possible pieces

	def __init__(self):
		m_color = -1
		m_type = -1

	def getPossibleActions(self, state):
					
		return None # never arrive here
	
	# vertical down moves
	def getVerticalDownMoves(self, state):
		l = []		
		agentColor = self.m_color
		row0, col0 = state.m_agentPos.row, state.m_agentPos.col

		# print('Accedo a movimientos verticales abajo')

		busyCell = False
		for r in range(row0+1,state.m_boardSize):
			if not busyCell:
				if state.m_board[r][col0] == Utils.empty: # add action
					action = Action(state.m_agentPos, Position(r,col0))
					l.append(action)
				else:
					busyCell = True
					if agentColor != Utils.getColorPiece(state.m_board[r][col0]): # capture piece
						action = Action(state.m_agentPos, Position(r,col0))
						l.append(action)
		
		return l
		
	# horizontal left moves
	def getHorizontalLeftMoves(self, state):
		l = []		
		agentColor = self.m_color
		row0, col0 = state.m_agentPos.row, state.m_agentPos.col
		# print('Accedo a movimientos horizontales izq')

		busyCell = False
		for c in range(col0-1,-1,-1):
			if not busyCell:
				if state.m_board[row0][c] == Utils.empty: # add action
					action = Action(state.m_agentPos, Position(row0,c))
					l.append(action)
				else:
					busyCell = True
					if agentColor != Utils.getColorPiece(state.m_board[row0][c]): # capture piece
						action = Action(state.m_agentPos, Position(row0,c))
						l.append(action)

		return l

	# horizontal right moves
	def getHorizontalRightMoves(self, state):
		l = []		
		agentColor = self.m_color
		row0, col0 = state.m_agentPos.row, state.m_agentPos.col

		# print('Accedo a movimientos horizontales dcha')

		busyCell = False
		for c in range(col0+1,state.m_boardSize):
			if not busyCell:
				if state.m_board[row0][c] == Utils.empty: # add action
					action = Action(state.m_agentPos, Position(row0,c))
					l.append(action)
				else:
					busyCell = True
					if agentColor != Utils.getColorPiece(state.m_board[row0][c]): # capture piece
						action = Action(state.m_agentPos, Position(row0,c))
						l.append(action)
		
		return l

	# vertical up moves
	def getVerticalUpMoves(self, state):
		l = []		
		agentColor = self.m_color
		row0, col0 = state.m_agentPos.row, state.m_agentPos.col

		# print('Accedo a movimientos verticales arriba')
		
		busyCell = False
		for r in range(row0-1,-1,-1):
			if not busyCell:
				if state.m_board[r][col0] == Utils.empty: # add action
					action = Action(state.m_agentPos, Position(r,col0))
					l.append(action)
				else:
					busyCell = True
					if agentColor != Utils.getColorPiece(state.m_board[r][col0]): # capture piece
						action = Action(state.m_agentPos, Position(r,col0))
						l.append(action)
		return l
			

	
	
	#  ---- Movimientos diagonales ----  HAY QUE ARREGLARLOS QUE POR ALGÚN MOTIVO HACE MOVIMIENTOS HORIZONTALES Y VERTICALES DE 1 EN 1

	
	# Abajo izquierda
	def getDiagonalDownLeftMoves(self, state):

		l = []
		agentColor = self.m_color
		row0, col0 = state.m_agentPos.row, state.m_agentPos.col
		busyCell = False

		# print('diagonal abajo izq')

		for r in range(row0+1,state.m_boardSize):
			if not busyCell and col0 > 0:

				col0 = col0-1

				if state.m_board[r][col0] == Utils.empty: # add action
					action = Action(state.m_agentPos, Position(r,col0))
					l.append(action)
				else:
					busyCell = True
					if agentColor != Utils.getColorPiece(state.m_board[r][col0]): # capture piece
						action = Action(state.m_agentPos, Position(r,col0))
						l.append(action)
		# print ("abajo izquierda")
		return l
		
	# Abajo derecha
	def getDiagonalDownRightMoves(self, state):
	

		l = []
		agentColor = self.m_color
		row0, col0 = state.m_agentPos.row, state.m_agentPos.col
		busyCell = False

		# print('diagonal abajo dcha')

		for r in range(row0+1,state.m_boardSize):
			if not busyCell and col0 < state.m_boardSize - 1:

				col0 = col0+1
				# print (col0)

				if state.m_board[r][col0] == Utils.empty: # add action
					action = Action(state.m_agentPos, Position(r,col0))
					l.append(action)
				else:
					busyCell = True
					if agentColor != Utils.getColorPiece(state.m_board[r][col0]): # capture piece
						action = Action(state.m_agentPos, Position(r,col0))
						l.append(action)
		return l

	# Arriba izquierda
	def getDiagonalUpLeftMoves(self, state):
		l = []
		agentColor = self.m_color
		row0, col0 = state.m_agentPos.row, state.m_agentPos.col
		busyCell = False

		# print('diagonal arriba izq')

		for r in range(row0-1,-1,-1):
			
			if not busyCell and col0 > 0:

				col0 = col0-1

				if state.m_board[r][col0] == Utils.empty: # add action
					action = Action(state.m_agentPos, Position(r,col0))
					l.append(action)
				else:
					busyCell = True
					if agentColor != Utils.getColorPiece(state.m_board[r][col0]): # capture piece
						action = Action(state.m_agentPos, Position(r,col0))
						l.append(action)
		return l

	# print ("arriba izquierda")
	# Arriba derecha
	def getDiagonalUpRightMoves(self, state):
		l = []
		agentColor = self.m_color
		row0, col0 = state.m_agentPos.row, state.m_agentPos.col
		busyCell = False

		# print('diagonal arriba dcha')

		for r in range(row0-1,-1,-1):
			if not busyCell and col0 < state.m_boardSize - 1:

				col0 = col0+1

				if state.m_board[r][col0] == Utils.empty: # add action
					action = Action(state.m_agentPos, Position(r,col0))
					l.append(action)
				else:
					busyCell = True
					if agentColor != Utils.getColorPiece(state.m_board[r][col0]): # capture piece
						action = Action(state.m_agentPos, Position(r,col0))
						l.append(action)
		return l


			
			
	

	