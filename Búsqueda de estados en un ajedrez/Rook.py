import Utils
from Piece import Piece

# this class implements the getPossibleActions for each type of piece
# Clase para la torre

class Rook(Piece): 
	
	# constructor
	def __init__(self, color):
		self.m_color = color
		
		if color==0: 
			self.m_type = Utils.wRook
		else:
			self.m_type = Utils.bRook

	
	# this method must be completed with all the possible pieces	
	def getPossibleActions(self, state):
		l = []

		l = self.getVerticalUpMoves(state)
		l += self.getHorizontalRightMoves(state)
		l += self.getHorizontalLeftMoves(state)
		l += self.getVerticalDownMoves(state)
		
		return l
