# This class contains the information needed to represent a state 
# and some useful methods

import sys
import copy
import Utils

class State:
	m_board = None
	m_agentPos = None
	m_agent = -1 # the type of piece
	m_color = 0  # 0 for white, 1 for black
	m_boardSize = -1 

	# Utilidad del estado
	utilidad_total = None

	# Utilidad que aportan las piezas
	utilidad_peon = None
	utilidad_caballo = None
	utilidad_torre = None
	utilidad_alfil = None
	utilidad_reina = None
	utilidad_rey = 20000
	
	# constructor
	# def __init__(self, board, position, agent):
	# 	self.m_board = board
	# 	self.m_agentPos = position
	# 	self.m_agent = agent
		
	# 	if (self.m_agent >11):
	# 		print("\n*** Invalid piece ***\n")
	# 		sys.exit(0)
	# 	else: 
	# 		if (self.m_agent >5):
	# 			self.m_color = 1 # black
		
	# 	self.m_boardSize = len(board[0])
	
	def __init__(self, board):
		self.m_board = board
		self.m_boardSize = len(board[0])

	# compares if the current state is final, i.e. the agent is in the last row
	def isFinal(self):
		if (self.m_agentPos.row == self.m_boardSize-1): 
			return True
		else: 
			return False
	
	# hard copy of an State
	def copy(self, memodict={}):
		#print '__deepcopy__(%s)' % str(memo)
		# newState = State(self.m_board, self.m_agentPos, self.m_agent)
		newState = State(self.m_board)
		newState.__dict__.update(self.__dict__)
		newState.m_board = copy.deepcopy(self.m_board, memodict)
		newState.m_agentPos = copy.deepcopy(self.m_agentPos, memodict)
		newState.m_agent = copy.deepcopy(self.m_agent, memodict)
		newState.m_color = copy.deepcopy(self.m_color, memodict)
		newState.m_boardSize = copy.deepcopy(self.m_boardSize, memodict)

		return newState
		
	# apply a given action over the current state -which remains unmodified. Return a new state
	
	def applyAction(self,action):
		newState = self.copy()
		newState.m_board[action.m_initPos.row][action.m_initPos.col] = Utils.empty
		newState.m_board[action.m_finalPos.row][action.m_finalPos.col] = newState.m_agent
		newState.m_agentPos = action.m_finalPos
		
		return newState
	
	def __eq__(self, other):
		if isinstance(other, State):
			return self.m_agentPos.row == other.m_agentPos.row and self.m_agentPos.col == other.m_agentPos.col and self.m_board == other.m_board

	def __hash__(self):
		return hash((self.m_boardSize))
	
	def calculaUtilidad(self, board):

		# Calcular la utilidad de un estado

		self.utilidad_total = 1000




