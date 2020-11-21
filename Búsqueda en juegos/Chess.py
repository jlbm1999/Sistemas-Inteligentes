import sys
import random
import Utils
from Position import Position
from Action import Action
from State import State
from Piece import Piece
from Rook import Rook
from Pawn import Pawn
from King import King
from Knight import Knight
from Queen import Queen
from Bishop import Bishop
from time import time


# if __name__ == '__main__':
#     if (len(sys.argv) < 6):
#         print("\n**Sorry, correct usage require 5 params:")
#         print("Board size: int.")
#         print("Density: (0.1,1]. Probability for each piece to be included.")
#         print("Seed: int. To initialize the problem instance random number generator (for reproducibility)")
#         print("Agent: {0,1,2,3,4,5} standing for white pawn, rook, bishop, knight, queen or king.")
#         print("Algorithm: String. Name of the algorithm")
#         print("If the algorithm requires depth, introduce it.")
#         sys.exit()

#     elif (len(sys.argv) < 7):
#         size = int(sys.argv[1])
#         density = float(sys.argv[2])
#         seed = int(sys.argv[3])
#         agent = int(sys.argv[4])
#         algoritmo = (sys.argv[5])

#         if size < 4:
#             print("\nSorry: board to small, modified to 4")
#             size = 4

#         if density<0.1 or density>1.0:
#             print("\nSorry: bad density value, modified to 0.25")
#             density = 0.25

#         if density*32 > size*size:
#             print("\nSorry: too much pieces for the board size, modifying density to 0.25")
#             density=0.25

#         if agent <0 or agent>11:
#             print("\nSorry: bad selected agent, modified to 1 (white rook)")
#             agent = Utils.wRook
        
#     elif (len(sys.argv) >= 7 and len(sys.argv) < 8):
#         size = int(sys.argv[1])
#         density = float(sys.argv[2])
#         seed = int(sys.argv[3])
#         agent = int(sys.argv[4])
#         algoritmo = (sys.argv[5])
#         profundidad = int(sys.argv[6])

#         if size < 4:
#             print("\nSorry: board to small, modified to 4")
#             size = 4

#         if density<0.1 or density>1.0:
#             print("\nSorry: bad density value, modified to 0.25")
#             density = 0.25

#         if density*32 > size*size:
#             print("\nSorry: too much pieces for the board size, modifying density to 0.25")
#             density=0.25

#         if agent <0 or agent>11:
#             print("\nSorry: bad selected agent, modified to 1 (white rook)")
#             agent = Utils.wRook

# método = minimax o alfabeta
# inicio = true o false
# profundidad = profundidad a la que se desarrolla el árbol
# color = white/black o todo o dummy
# jugadas = 5  Numero de jugadas
probabilidad = 0.5
seed = 38



initState = Utils.getChessInstancePosition(probabilidad, seed)  # Instancia en concreto
# initState = Utils.getChessInstance(probabilidad, seed)        # Instancia inicial
Utils.printBoard(initState)
# search = Algoritmos(nodoInicial, seed)


# if search.m_finalState == None:
#     print("\nSorry, no solution found ....")
# else:
#     print("Solution length: %d" % (len(search.solucion) - 1))       # Restamos 1 porque el nodo inicial no cuenta  
#     print("Solution cost:   %f" % search.finalCost)
#     print("Solution time:   %f" % t)

#     print("Solution:\n")
#     search.solucion.reverse()                                       # Para que los movimientos salgan ordenados
#     for i in range(len(search.solucion) - 1):                       # -1 porque quitamos el inicial
#         print("%d : " % (i + 1), end="")
#         print(search.solucion[i + 1].accion)
#     print()
#     Utils.printBoard(search.m_finalState)