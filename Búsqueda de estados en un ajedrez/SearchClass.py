
# Clase donde se modelarán los algoritmos de búsqueda informada y no informada
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
import copy

# Estructuras de datos que necesitamos (cola, pila, cola de prioridad)
from collections import deque
from queue import PriorityQueue

class SearchClass:

    # member variables
    m_initialState = None
    m_initialNode = None
    m_seedRS = -1
    solucion = None
    finalCost = None
    nodosGenerados = 0
    nodosExpandidos = 0

    m_cost = 0
    m_piece = Piece()
    m_finalState = None

    # Constructor de la clase
    def __init__(self, nodo, seed):
        
        self.m_initialNode = nodo
        self.m_initialState = nodo.state
        self.m_seedRS = seed
        self.m_cost = 0
        self.solucion = []  # Lista de las acciones que hace el agente desde el estado inicial al estado final, en forma de nodos
        random.seed(seed)
        s0 = self.m_initialNode.state

        if s0.m_agent == Utils.wPawn: 
            self.m_piece = Pawn(0)
        elif s0.m_agent == Utils.bPawn:
            self.m_piece = Pawn(1)
        elif s0.m_agent == Utils.wRook: 
            self.m_piece = Rook(0)
        elif s0.m_agent == Utils.bRook:
            self.m_piece = Rook(1)
        elif s0.m_agent == Utils.wKing:
            self.m_piece = King(0)
        elif s0.m_agent == Utils.bKing:
            self.m_piece = King(1)
        elif s0.m_agent == Utils.wKnight:
            self.m_piece = Knight(0)
        elif s0.m_agent == Utils.bKnight:
            self.m_piece = Knight(1)
        elif s0.m_agent == Utils.wBishop:
            self.m_piece = Bishop(0)
        elif s0.m_agent == Utils.bBishop:
            self.m_piece = Bishop(1)
        elif s0.m_agent == Utils.wQueen:
            self.m_piece = Queen(0)
        elif s0.m_agent == Utils.bQueen:
            self.m_piece = Queen(1)
        else:
            print("Chess piece not implemented")
            sys.exit()


            ################################ Métodos para gestionar las estructuras de datos y la heurística ################################


    # Utilizaremos este método para sacar de la forma correspondiente los nodos que vayamos a explorar
    def removeItem(self, estructura, algoritmo):
        if(algoritmo == "Anchura"):  
                return estructura.popleft()                # Como es una cola, sacamos por la izquierda
        elif(algoritmo == "Profundidad" or algoritmo == "profundidadLimitada" or algoritmo == "profundidadIterativa"):   
                return estructura.pop()                    # Como es una pila, hacemos un pop
        elif(algoritmo == 'CosteUniforme'):
                return estructura.get()[1]                 # Como es una cola de prioridad, sacamos el primer elemento, el cual es una tupla (coste, nodo), y nos quedamos con el nodo
        elif(algoritmo == 'PrimeroMejor' or algoritmo == 'A*'):
                return estructura.get()[1]
    

    # Utilizaremos este método para insertar de forma correspondiente los nodos que se vayan generando
    def insertItem(self, estructura, algoritmo, nodo, coste, heuristica):
        if(algoritmo == 'CosteUniforme'):
            estructura.put((coste, nodo))                  # Introducimos en la cola de prioridad la tupla (coste, nodo)
        elif((algoritmo == 'Profundidad') or (algoritmo == 'Anchura') or algoritmo == "profundidadLimitada" or algoritmo == "profundidadIterativa"):
            estructura.append(nodo)                        # Introducimos en la lista el nodo, ya que en anchura y en profunidad se insertan desde el mismo lado
        elif(algoritmo == 'PrimeroMejor' or algoritmo == 'A*'):
            estructura.put((heuristica, nodo))


    def calculaHeuristica(self, nodo, algoritmo):
        if(algoritmo == 'PrimeroMejor'):
            return ((nodo.state.m_boardSize - 1) - nodo.state.m_agentPos.row)                   # Nos quedamos con la distancia a la última columna f(n) = h(n)
        else:
            return (((nodo.state.m_boardSize - 1) - nodo.state.m_agentPos.row) + nodo.cost)     # Es la suma de la heurística y el coste f(n) = g(n) + h(n)


    
                                     ################################ Métodos de búsqueda ################################



    # Búsqueda no informada
    def busquedaNoInformada(self, nodoInicial, algoritmo):
        search = SearchClass(nodoInicial, algoritmo)        # Variable que usaremos para llamar a los métodos de la clase
        cerrado = set()                                        # Diccionario es la mejor estructura de datos para los nodos ya explorados
        nodosHijo = []                                      # Nodos que se generan cuando expandimos un nodo
        self.nodosGenerados = 1
        self.nodosExpandidos = 0

        # Inicializamos la estructura de datos como corresponda en función de la estrategia que vayamos a seguir
        estructura = deque()
        estructura.append(nodoInicial)                      # Para la búsqueda en anchura y en profundidad, la inserción de los nodos se realiza de la misma manera
        
        while (estructura):
            nodo = search.removeItem(estructura, algoritmo)     # Sacamos el nodo inicial de la estructura de datos en la que se encuentre

            if(nodo.state not in cerrado):                   # Buscamos si el estado se encuentra explorado
                if(nodo.goalNode()):                                # Comprobamos si el nodo es solución
                    self.m_finalState = nodo.state                  # Nos guardamos el estado final
                    self.finalCost = nodo.cost                      # Nos guardamos el coste final

                    while(nodo.padre != None):                      # Hasta que no lleguemos al nodo inicial, cuyo padre es null, no paramos
                        self.solucion.append(nodo)
                        nodo = nodo.padre

                    self.solucion.append(nodo)                      # Cuando llegamos al padre, lo sacamos a mano
                    # print('Algoritmo usado: ', algoritmo)
                    # print('Nodos generados: ', self.nodosGenerados)
                    # print('Nodos expandidos: ',self.nodosExpandidos)
                    return self.solucion                            # Devolvemos la lista con los nodos solución
                
                self.nodosExpandidos = self.nodosExpandidos + 1
                nodosHijo = self.m_piece.getPossibleActions(nodo.state)    # Depende de la pieza, se almacenan sus posibles movimientos
                self.nodosGenerados = self.nodosGenerados + len(nodosHijo)
                for i in nodosHijo:     #Aquí estamos iterando posibles movimientos, no estados 
                    nodoCopia = Node(nodo, i, copy.deepcopy(nodo.state, {}), nodo.cost, (0,0) , None, nodo.profundidad + 1)   # Generamos una copia del nodo actual para no modificarlo
                    nodoCopia.state = nodoCopia.state.applyAction(i)                                    # Le aplicamos la acción
                    nodoCopia.pos = (nodoCopia.state.m_agentPos.row, nodoCopia.state.m_agentPos.col)    # Actualizamos su posición

                    # Ahora, siguiendo la fórmula para aplicar el coste, actualizamos el coste del nodo
                    nodoCopia.cost = nodoCopia.cost + max(abs(nodo.state.m_agentPos.row - nodoCopia.state.m_agentPos.row), abs(nodo.state.m_agentPos.col - nodoCopia.state.m_agentPos.col)) + 1
                    search.insertItem(estructura, algoritmo, nodoCopia, nodoCopia.cost, nodoCopia.heuristic)     # Por último, insertamos el nodo generado en la estructura que le corresponda
                    
                nodosHijo = []              # Vaciamos la lista de nodos hijos para poder utilizarla más tarde
                cerrado.add(nodo.state)    # Insertamos la posición del agente en la lista de cerrados, para que no puedan repetirse 2 veces el mismo estado 
    
        return None
        
        
    # Búsqueda informada
    def busquedaInformada(self, nodoInicial, algoritmo):
        search = SearchClass(nodoInicial, algoritmo)        # Variable que usaremos para llamar a los métodos de la clase
        cerrado = set()                                       # Diccionario es la mejor estructura de datos para los nodos ya explorados
        nodosHijo = []                                      # Nodos que se generan cuando expandimos un nodo
        nodosGenerados = 1
        nodosExpandidos = 0
        estructura = PriorityQueue()

        if(algoritmo == 'CosteUniforme'):   # Aunque no sea búsqueda informada, nos conviene tenerlo aquí para ahorrar código
            estructura.put((nodoInicial.cost, nodoInicial))         # Como el Coste Uniforme utiliza una cola de prioridad, la inicializamos y le asignamos el valor del nodo inicial
        else:                                                       # Para la búsqueda informada, una cola de prioridad es la mejor opción, para comparar por la heurística
            estructura.put((nodoInicial.heuristic, nodoInicial))    # Tanto si es Primero mejor como A*, el f(nodoInicial) será el valor de la heurística, porque su coste es siempre 0

        while (estructura.qsize() > 0):

            nodo = search.removeItem(estructura, algoritmo)     # Sacamos el nodo inicial de la estructura de datos en la que se encuentre
            # Utils.printBoard(nodo.state)
            if(nodo.state not in cerrado):                            # Buscamos si el estado se encuentra explorado
                if(nodo.goalNode()):                                # Comprobamos si el nodo es solución
                    self.m_finalState = nodo.state                  # Nos guardamos el estado final
                    self.finalCost = nodo.cost                      # Nos guardamos el coste final

                    while(nodo.padre != None):                      # Hasta que no lleguemos al nodo inicial, cuyo padre es null, no paramos
                        self.solucion.append(nodo)
                        nodo = nodo.padre

                    self.solucion.append(nodo)                      # Cuando llegamos al padre, lo sacamos a mano
                    # print('Algoritmo usado: ', algoritmo)
                    # print('Nodos generados: ', nodosGenerados)
                    # print('Nodos expandidos: ', nodosExpandidos)
                    return self.solucion                            # Devolvemos la lista con los nodos solución
                
                nodosExpandidos = nodosExpandidos + 1
                nodosHijo = self.m_piece.getPossibleActions(nodo.state)    # Depende de la pieza, se almacenan sus posibles movimientos
                nodosGenerados = nodosGenerados + len(nodosHijo)

                for i in nodosHijo:     #Aquí estamos iterando posibles movimientos, no estados 
                    nodoCopia = Node(nodo, i, copy.deepcopy(nodo.state, {}), nodo.cost, (0,0) , search.calculaHeuristica(nodo, algoritmo), nodo.profundidad + 1)   # Generamos una copia del nodo actual para no modificarlo
                    nodoCopia.state = nodoCopia.state.applyAction(i)                                    # Le aplicamos la acción
                    nodoCopia.pos = (nodoCopia.state.m_agentPos.row, nodoCopia.state.m_agentPos.col)    # Actualizamos su posición
                   
                    # Ahora, siguiendo la fórmula para aplicar el coste, actualizamos el coste del nodo
                    nodoCopia.cost = nodoCopia.cost + max(abs(nodo.state.m_agentPos.row - nodoCopia.state.m_agentPos.row), abs(nodo.state.m_agentPos.col - nodoCopia.state.m_agentPos.col)) + 1 
                    nodoCopia.heuristic = search.calculaHeuristica(nodoCopia, algoritmo)                           # Actualizamos la heurística
                    search.insertItem(estructura, algoritmo, nodoCopia, nodoCopia.cost, nodoCopia.heuristic)     # Por último, insertamos el nodo generado en la estructura que le corresponda
                    
                nodosHijo = []              # Vaciamos la lista de nodos hijos para poder utilizarla más tarde
                cerrado.add(nodo.state)    # Insertamos la posición del agente en la lista de cerrados, para que no puedan repetirse 2 veces el mismo estado 
        
        return None

    
                                     ################################ Métodos opcionales ################################

    def profundidadLimitada(self, nodoInicial, algoritmo, profundidad):
        cerrado = set()                                       # Diccionario es la mejor estructura de datos para los nodos ya explorados
        nodosHijo = []                                      # Nodos que se generan cuando expandimos un nodo
        nodosGenerados = 1
        nodosExpandidos = 0
        limite = 0

        estructura = deque()
        estructura.append(nodoInicial)                     

        while (estructura):

            nodo = estructura.pop()     # Sacamos el nodo inicial de la estructura de datos en la que se encuentre

            if(nodo.state not in cerrado):                   # Buscamos si el estado se encuentra explorado
                if(nodo.goalNode()):                                # Comprobamos si el nodo es solución
                    self.m_finalState = nodo.state                  # Nos guardamos el estado final
                    self.finalCost = nodo.cost                      # Nos guardamos el coste final

                    while(nodo.padre != None):                      # Hasta que no lleguemos al nodo inicial, cuyo padre es null, no paramos
                        self.solucion.append(nodo)
                        nodo = nodo.padre

                    self.solucion.append(nodo)                      # Cuando llegamos al padre, lo sacamos a mano
                    # print('Algoritmo usado: ', algoritmo)
                    # print('Nodos generados: ', nodosGenerados)
                    # print('Nodos expandidos: ', nodosExpandidos)
                    # print('Profundidad: ', profundidad)
                    return self.solucion                            # Devolvemos la lista con los nodos solución      
                if(nodo.profundidad != profundidad):
                    nodosExpandidos = nodosExpandidos + 1
                    nodosHijo = self.m_piece.getPossibleActions(nodo.state)    # Depende de la pieza, se almacenan sus posibles movimientos

                    for i in nodosHijo:     #Aquí estamos iterando posibles movimientos, no estados 
                        nodosGenerados = nodosGenerados + 1
                        nodoCopia = Node(nodo, i, copy.deepcopy(nodo.state, {}), nodo.cost, (0,0) , None, nodo.profundidad + 1)   # Generamos una copia del nodo actual para no modificarlo
                        nodoCopia.state = nodoCopia.state.applyAction(i)                                    # Le aplicamos la acción
                        nodoCopia.pos = (nodoCopia.state.m_agentPos.row, nodoCopia.state.m_agentPos.col)    # Actualizamos su posición

                        # Ahora, siguiendo la fórmula para aplicar el coste, actualizamos el coste del nodo
                        nodoCopia.cost = nodoCopia.cost + max(abs(nodo.state.m_agentPos.row - nodoCopia.state.m_agentPos.row), abs(nodo.state.m_agentPos.col - nodoCopia.state.m_agentPos.col)) + 1
                        estructura.append(nodoCopia)     
                    
                nodosHijo = []              # Vaciamos la lista de nodos hijos para poder utilizarla más tarde
                cerrado.add(nodo.pos)    # Insertamos la posición del agente en la lista de cerrados, para que no puedan repetirse 2 veces el mismo estado 

        
        return None
        


    def profundidadIterativa(self, nodoInicial, algoritmo, profundidad):
        cerrado = set()                                        # Diccionario es la mejor estructura de datos para los nodos ya explorados
        nodosHijo = []                                      # Nodos que se generan cuando expandimos un nodo
        nodosGenerados = 1
        nodosExpandidos = 0
        limite = 0

        estructura = deque()
        estructura.append(nodoInicial)
        finales = deque()
        inicial = False               

        while (estructura):

            #print ("bucle")
            nodo = estructura.pop()     # Sacamos el nodo inicial de la estructura de datos en la que se encuentre
            
            if (len(estructura) == 0 and inicial):
                profundidad = profundidad + 1
                estructura = copy.copy(finales)
                finales = deque()
            inicial = True

            if(nodo.state not in cerrado):                   # Buscamos si el estado se encuentra explorado
                if(nodo.goalNode()):                                # Comprobamos si el nodo es solución
                    self.m_finalState = nodo.state                  # Nos guardamos el estado final
                    self.finalCost = nodo.cost                      # Nos guardamos el coste final

                    while(nodo.padre != None):                      # Hasta que no lleguemos al nodo inicial, cuyo padre es null, no paramos
                        self.solucion.append(nodo)
                        nodo = nodo.padre

                    self.solucion.append(nodo)                      # Cuando llegamos al padre, lo sacamos a mano
                    # print('Algoritmo usado: ', algoritmo)
                    # print('Nodos generados: ', nodosGenerados)
                    # print('Nodos expandidos: ', nodosExpandidos)
                    # print('Profundidad: ', profundidad)
                    return self.solucion                            # Devolvemos la lista con los nodos solución
                if(nodo.profundidad != profundidad):
                    nodosExpandidos = nodosExpandidos + 1
                    nodosHijo = self.m_piece.getPossibleActions(nodo.state)    # Depende de la pieza, se almacenan sus posibles movimientos

                    for i in nodosHijo:     #Aquí estamos iterando posibles movimientos, no estados 
                        nodosGenerados = nodosGenerados + 1
                        nodoCopia = Node(nodo, i, copy.deepcopy(nodo.state, {}), nodo.cost, (0,0) , None, nodo.profundidad + 1)   # Generamos una copia del nodo actual para no modificarlo
                        nodoCopia.state = nodoCopia.state.applyAction(i)                                    # Le aplicamos la acción
                        nodoCopia.pos = (nodoCopia.state.m_agentPos.row, nodoCopia.state.m_agentPos.col)    # Actualizamos su posición

                        # Ahora, siguiendo la fórmula para aplicar el coste, actualizamos el coste del nodo
                        nodoCopia.cost = nodoCopia.cost + max(abs(nodo.state.m_agentPos.row - nodoCopia.state.m_agentPos.row), abs(nodo.state.m_agentPos.col - nodoCopia.state.m_agentPos.col)) + 1
                        estructura.append(nodoCopia)
                nodosHijo = []              # Vaciamos la lista de nodos hijos para poder utilizarla más tarde
                if(nodo.profundidad < profundidad):
                    cerrado.add(nodo.pos)    # Insertamos la posición del agente en la lista de cerrados, para que no puedan repetirse 2 veces el mismo estado
                else:
                    finales.append(nodo)

        
        return None




    
