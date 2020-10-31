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
from Node import Node
from SimpleRandomSearch import SimpleRandomSearch
from SearchClass import SearchClass
from time import time
from matplotlib import pyplot
import numpy as np
from tabulate import tabulate



size = 8
density = 1.0
seed = 1
agent = 0
agentes = [0,1,2,3,4,5]
algoritmos = ['Anchura', 'Profundidad', 'CosteUniforme', 'PrimeroMejor', 'A*', 'ProfundidadLimitada', 'ProfundidadIterativa']
profundidad = 20

initState = Utils.getProblemInstance(size, density, seed, agent)
nodoInicial = Node(None, None, initState, 0, (initState.m_agentPos.row, initState.m_agentPos.col), initState.m_boardSize - 1, 0)
search = SearchClass(nodoInicial, seed)



tamaño = list(range(8, 16, 1))


peon = np.array([])
torre = np.array([])
alfil = np.array([])
caballo = np.array([])
reina = np.array([])
rey = np.array([])

# TIEMPOS
tiemposAnchura = [] # En principio, de 0-9 es el peón, de 10-19 es la torre, etc
tiemposProfundidad = []
tiemposCosteUniforme = []
tiemposPrimeroMejor = []
tiemposAstar = []
tiemposProfundidadLimitada = []
tiemposProfundidadIterativa = []

# NODOS GENERADOS
NGAnchura = []
NGProfundidad = []
NGCosteUniforme = []
NGPrimeroMejor = []
NGAstar = []
NGProfundidadLimitada = []
NGProfundidadIterativa = []

# NODOS EXPANDIDOS
NEAnchura = []
NEProfundidad = []
NECosteUniforme = []
NEPrimeroMejor = []
NEAstar = []
NEProfundidadLimitada = []
NEProfundidadIterativa = []

# COSTE DE LA SOLUCIÓN

costeAnchura = []
costeProfundidad = []
costeCosteUniforme = []
costePrimeroMejor = []
costeAstar = []
costeProfundidadLimitada = []
costeProfundidadIterativa = []

headers =['Tamaño', 'Anchura', 'Profundidad', 'CosteUniforme', 'PrimeroMejor', 'Astar', 'ProfundidadLimitada', 'ProfundidadIterativa']


for s in tamaño:
    for i in agentes:
        agent = i
        for k in range(10):
            seed = k + 10
            initState = Utils.getProblemInstance(size, density, seed, agent)
            nodoInicial = Node(None, None, initState, 0, (initState.m_agentPos.row, initState.m_agentPos.col), initState.m_boardSize - 1, 0)
            search = SearchClass(nodoInicial, seed)
            for j in algoritmos:
                algoritmo = j
                if(algoritmo == 'Anchura'):
                    t = time()
                    sol = search.busquedaNoInformada(nodoInicial, algoritmo)
                    t = time() - t
                    tiemposAnchura.append(t)
                    NGAnchura.append(search.nodosGenerados)
                    NEAnchura.append(search.nodosExpandidos)
                    costeAnchura.append(search.finalCost)
                elif(algoritmo == 'Profundidad'):
                    t = time()
                    sol = search.busquedaNoInformada(nodoInicial, algoritmo)
                    t = time() - t
                    tiemposProfundidad.append(t)
                    NGProfundidad.append(search.nodosGenerados)
                    NEProfundidad.append(search.nodosExpandidos)
                    costeProfundidad.append(search.finalCost)
                elif(algoritmo == 'CosteUniforme'):
                    t = time()
                    sol = search.busquedaInformada(nodoInicial, algoritmo)
                    t = time() - t
                    tiemposCosteUniforme.append(t)
                    NGCosteUniforme.append(search.nodosGenerados)
                    NECosteUniforme.append(search.nodosExpandidos)
                    costeCosteUniforme.append(search.finalCost)
                elif(algoritmo == 'ProfundidadLimitada'):
                    t = time()
                    sol = search.profundidadLimitada(nodoInicial, algoritmo, profundidad)
                    t = time() - t
                    tiemposProfundidadLimitada.append(t)
                    NGProfundidadLimitada.append(search.nodosGenerados)
                    NEProfundidadLimitada.append(search.nodosExpandidos)
                    costeProfundidadLimitada.append(search.finalCost)
                elif(algoritmo == 'ProfundidadIterativa'):
                    t = time()
                    sol = search.profundidadIterativa(nodoInicial, algoritmo, profundidad)
                    t = time() - t
                    tiemposProfundidadIterativa.append(t)
                    NGProfundidadIterativa.append(search.nodosGenerados)
                    NEProfundidadIterativa.append(search.nodosExpandidos)
                    costeProfundidadIterativa.append(search.finalCost)
                elif(algoritmo == 'A*'):
                    t = time()
                    sol = search.busquedaInformada(nodoInicial, algoritmo)
                    t = time() - t
                    tiemposAstar.append(t)
                    NGAstar.append(search.nodosGenerados)
                    NEAstar.append(search.nodosExpandidos)
                    costeAstar.append(search.finalCost)
                else:
                    t = time()
                    sol = search.busquedaInformada(nodoInicial, algoritmo)
                    t = time() - t
                    tiemposPrimeroMejor.append(t)
                    NGPrimeroMejor.append(search.nodosGenerados)
                    NEPrimeroMejor.append(search.nodosExpandidos)
                    costePrimeroMejor.append(search.finalCost)

    peon_t = np.array([s, tiemposAnchura[:10], tiemposProfundidad[:10], tiemposCosteUniforme[:10], tiemposPrimeroMejor[:10], tiemposAstar[:10], tiemposProfundidadLimitada[:10], tiemposProfundidadIterativa[:10]])
    torre_t = np.array([s, tiemposAnchura[10:20], tiemposProfundidad[10:20], tiemposCosteUniforme[10:20], tiemposPrimeroMejor[10:20], tiemposAstar[10:20], tiemposProfundidadLimitada[10:20], tiemposProfundidadIterativa[10:20]])
    alfil_t = np.array([s, tiemposAnchura[20:30], tiemposProfundidad[20:30], tiemposCosteUniforme[20:30], tiemposPrimeroMejor[20:30], tiemposAstar[20:30], tiemposProfundidadLimitada[20:30], tiemposProfundidadIterativa[20:30]])
    caballo_t = np.array([s, tiemposAnchura[30:40], tiemposProfundidad[30:40], tiemposCosteUniforme[30:40], tiemposPrimeroMejor[30:40], tiemposAstar[30:40], tiemposProfundidadLimitada[30:40], tiemposProfundidadIterativa[30:40]])
    reina_t = np.array([s, tiemposAnchura[40:50], tiemposProfundidad[40:50], tiemposCosteUniforme[40:50], tiemposPrimeroMejor[40:50], tiemposAstar[40:50], tiemposProfundidadLimitada[40:50], tiemposProfundidadIterativa[40:50]])
    rey_t = np.array([s, tiemposAnchura[50:60], tiemposProfundidad[50:60], tiemposCosteUniforme[50:60], tiemposPrimeroMejor[50:60], tiemposAstar[50:60], tiemposProfundidadLimitada[50:60], tiemposProfundidadIterativa[50:60]])

    peon_ng = np.array([s, NGAnchura[:10], NGProfundidad[:10], NGCosteUniforme[:10], NGPrimeroMejor[:10], NGAstar[:10], NGProfundidadLimitada[:10], NGProfundidadIterativa[:10]])
    torre_ng = np.array([s, NGAnchura[10:20], NGProfundidad[10:20], NGCosteUniforme[10:20], NGPrimeroMejor[10:20], NGAstar[10:20], tiemposProfundidadLimitada[10:20], NGProfundidadIterativa[10:20]])
    alfil_ng = np.array([s, NGAnchura[20:30], NGProfundidad[20:30], NGCosteUniforme[20:30], NGPrimeroMejor[20:30], NGAstar[20:30], tiemposProfundidadLimitada[20:30], NGProfundidadIterativa[20:30]])
    caballo_ng = np.array([s, NGAnchura[30:40], NGProfundidad[30:40], NGCosteUniforme[30:40], NGPrimeroMejor[30:40], NGAstar[30:40], tiemposProfundidadLimitada[30:40], NGProfundidadIterativa[30:40]])
    reina_ng = np.array([s, NGAnchura[40:50], NGProfundidad[40:50], NGCosteUniforme[40:50], NGPrimeroMejor[40:50], NGAstar[40:50], tiemposProfundidadLimitada[40:50], NGProfundidadIterativa[40:50]])
    rey_ng = np.array([s, NGAnchura[50:60], NGProfundidad[50:60], NGCosteUniforme[50:60], NGPrimeroMejor[50:60], NGAstar[50:60], tiemposProfundidadLimitada[50:60], NGProfundidadIterativa[50:60]])

    peon_ne = np.array([s, NEAnchura[:10], NEProfundidad[:10], NECosteUniforme[:10], NEPrimeroMejor[:10], NEAstar[:10], NEProfundidadLimitada[:10], NEProfundidadIterativa[:10]])
    torre_ne = np.array([s, NEAnchura[10:20], NEProfundidad[10:20], NECosteUniforme[10:20], NEPrimeroMejor[10:20], NEAstar[10:20], NEProfundidadLimitada[10:20], NEProfundidadIterativa[10:20]])
    alfil_ne = np.array([s, NEAnchura[20:30], NEProfundidad[20:30], NECosteUniforme[20:30], NEPrimeroMejor[20:30], NEAstar[20:30], NEProfundidadLimitada[20:30], NEProfundidadIterativa[20:30]])
    caballo_ne = np.array([s, NEAnchura[30:40], NEProfundidad[30:40], NECosteUniforme[30:40], NEPrimeroMejor[30:40], NEAstar[30:40], NEProfundidadLimitada[30:40], NEProfundidadIterativa[30:40]])
    reina_ne = np.array([s, NEAnchura[40:50], NEProfundidad[40:50], NECosteUniforme[40:50], NEPrimeroMejor[40:50], NEAstar[40:50], NEProfundidadLimitada[40:50], NEProfundidadIterativa[40:50]])
    rey_ne = np.array([s, NEAnchura[50:60], NEProfundidad[50:60], NECosteUniforme[50:60], NEPrimeroMejor[50:60], NEAstar[50:60], NEProfundidadLimitada[50:60], NEProfundidadIterativa[50:60]])

    peon_c = np.array([s, costeAnchura[:10], costeProfundidad[:10], costeCosteUniforme[:10], costePrimeroMejor[:10], costeAstar[:10], costeProfundidadLimitada[:10], costeProfundidadIterativa[:10]])
    torre_c = np.array([s, costeAnchura[10:20], costeProfundidad[10:20], costeCosteUniforme[10:20], costePrimeroMejor[10:20], costeAstar[10:20], costeProfundidadLimitada[10:20], costeProfundidadIterativa[10:20]])
    alfil_c = np.array([s, costeAnchura[20:30], costeProfundidad[20:30], costeCosteUniforme[20:30], costePrimeroMejor[20:30], costeAstar[20:30], costeProfundidadLimitada[20:30], costeProfundidadIterativa[20:30]])
    caballo_c = np.array([s, costeAnchura[30:40], costeProfundidad[30:40], costeCosteUniforme[30:40], costePrimeroMejor[30:40], costeAstar[30:40], costeProfundidadLimitada[30:40], costeProfundidadIterativa[30:40]])
    reina_c = np.array([s, costeAnchura[40:50], costeProfundidad[40:50], costeCosteUniforme[40:50], costePrimeroMejor[40:50], costeAstar[40:50], costeProfundidadLimitada[40:50], costeProfundidadIterativa[40:50]])
    rey_c = np.array([s, costeAnchura[50:60], costeProfundidad[50:60], costeCosteUniforme[50:60], costePrimeroMejor[50:60], costeAstar[50:60], costeProfundidadLimitada[50:60], costeProfundidadIterativa[50:60]])

    peon = np.append(peon, [peon_t, peon_ng, peon_ne, peon_c])
    torre = np.append(torre, [torre_t, torre_ng, torre_ne, torre_c])
    alfil = np.append(alfil, [alfil_t, alfil_ng, alfil_ne, alfil_c])
    caballo = np.append(caballo, [caballo_t, caballo_ng, caballo_ne, caballo_c])
    reina = np.append(reina, [reina_t, reina_ng, reina_ne, reina_c])
    rey = np.append(rey, [rey_t, rey_ng, rey_ne, rey_c])


    # for i in range(4):
    #     print("\nPeón:\n")
    #     print(tabulate(peon[i].transpose(),headers,tablefmt="fancy_grid"))
    #     print("\nTorre:\n")
    #     print(tabulate(torre[i].transpose(),headers,tablefmt="fancy_grid"))
    #     print("\nAlfil:\n")
    #     print(tabulate(alfil[i].transpose(),headers,tablefmt="fancy_grid"))
    #     print("\nCaballo:\n")
    #     print(tabulate(caballo[i].transpose(),headers,tablefmt="fancy_grid"))
    #     print("\nReina:\n")
    #     print(tabulate(reina[i].transpose(),headers,tablefmt="fancy_grid"))
    #     print("\nRey:\n")
    #     print(tabulate(rey[i].transpose(),headers,tablefmt="fancy_grid"))

print(len(peon))
