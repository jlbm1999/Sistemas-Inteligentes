
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

class Algoritmos:

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
        # Como es una cola, sacamos por la izquierda
        if(algoritmo == "Anchura"):  
            return estructura.popleft()                
        elif(algoritmo == "Profundidad" or algoritmo == "profundidadLimitada" or algoritmo == "profundidadIterativa"):   
            # Como es una pila, hacemos un pop
            return estructura.pop()                    
        else:
            # Como es una cola de prioridad, sacamos el primer elemento, el cual es una tupla (coste, nodo), y nos quedamos con el nodo
            return estructura.get()[1]                 

    
    # Utilizaremos este método para insertar de forma correspondiente los nodos que se vayan generando
    def insertItem(self, estructura, algoritmo, nodo, coste, heuristica):
        if(algoritmo == 'CosteUniforme'):
            # Introducimos en la cola de prioridad la tupla (coste, nodo)
            estructura.put((coste, nodo))                       
        elif((algoritmo == 'Profundidad') or (algoritmo == 'Anchura') or algoritmo == "profundidadLimitada" or algoritmo == "profundidadIterativa"):
            # Introducimos en la lista el nodo, ya que en anchura y en profunidad se insertan desde el mismo lado
            estructura.append(nodo)                             
        elif(algoritmo == 'PrimeroMejor' or algoritmo == 'A*'):
            # Introducimos en la cola de prioridad la tupla (heurística, nodo)
            estructura.put((heuristica, nodo))              


    def calculaHeuristica(self, nodo, algoritmo):
        if(algoritmo == 'PrimeroMejor'):
            # Nos quedamos con la distancia a la última columna f(n) = h(n) (Primero Mejor)
            return ((nodo.state.m_boardSize - 1) - nodo.state.m_agentPos.row)                   
        elif (algoritmo == 'A*'):
            # Es la suma de la heurística y el coste f(n) = g(n) + h(n)  (A*)
            return (((nodo.state.m_boardSize - 1) - nodo.state.m_agentPos.row) + nodo.cost)     
        else:
             # Devolvemos el coste del nodo (Coste Uniforme)
            return nodo.cost                   

                                     ################################ Métodos de búsqueda ################################



    # Búsqueda no informada
    def busquedaNoInformada(self, nodoInicial, algoritmo):
        search = Algoritmos(nodoInicial, algoritmo)             # Variable que usaremos para llamar a los métodos de la clase
        cerrado = set()                                         # Un set es la mejor estructura de datos para los estados ya explorados
        nodosHijo = []                                          # Nodos que se generan cuando expandimos un nodo
        self.nodosGenerados = 1
        self.nodosExpandidos = 0

        estructura = deque()                                    # La estructura a usar será o una cola o una pila en función del algoritmo.
        estructura.append(nodoInicial)

        while (estructura):

            nodo = search.removeItem(estructura, algoritmo)         # Sacamos el nodo inicial de la estructura de datos en la que se encuentre
            if(nodo.state not in cerrado):                          # Buscamos si el estado se encuentra explorado
                if(nodo.goalNode()):                                # Comprobamos si el nodo es solución
                    self.m_finalState = nodo.state                  # Nos guardamos el estado final
                    self.finalCost = nodo.cost                      # Nos guardamos el coste final

                    while(nodo.padre != None):                      # Hasta que no lleguemos al nodo inicial, cuyo padre es null, no paramos
                        self.solucion.append(nodo)
                        nodo = nodo.padre

                    self.solucion.append(nodo)                      # Cuando llegamos al padre, lo sacamos a mano
                    print('Algoritmo usado: ', algoritmo)
                    print('Nodos generados: ', self.nodosGenerados)
                    print('Nodos expandidos: ',self.nodosExpandidos)
                    return self.solucion                            # Devolvemos la lista con los nodos solución
                
                self.nodosExpandidos = self.nodosExpandidos + 1
                nodosHijo = self.m_piece.getPossibleActions(nodo.state)         # Depende de la pieza, se almacenan sus posibles movimientos
                self.nodosGenerados = self.nodosGenerados + len(nodosHijo)      # Contamos los hijos generados

                # Aquí estamos iterando posibles movimientos, no estados
                for i in nodosHijo:                                             
                    # Generamos una copia del nodo actual para no modificarlo 
                    nodoCopia = Node(nodo, i, copy.deepcopy(nodo.state, {}).applyAction(i)  , nodo.cost, (0,0) , None, nodo.profundidad + 1)   
                    nodoCopia.pos = (nodoCopia.state.m_agentPos.row, nodoCopia.state.m_agentPos.col)    # Actualizamos su posición

                    # Ahora, siguiendo la fórmula para aplicar el coste, actualizamos el coste del nodo
                    nodoCopia.cost = nodoCopia.cost + max(abs(nodo.state.m_agentPos.row - nodoCopia.state.m_agentPos.row), abs(nodo.state.m_agentPos.col - nodoCopia.state.m_agentPos.col)) + 1
                    search.insertItem(estructura, algoritmo, nodoCopia, nodoCopia.cost, nodoCopia.heuristic)     # Por último, insertamos el nodo generado en la estructura que le corresponda
                    
                nodosHijo = []              # Vaciamos la lista de nodos hijos para poder utilizarla más tarde
                cerrado.add(nodo.state)     # Insertamos el estado para que no pueda volver a explorarse
        return None
        
        
    # Búsqueda informada
    def busquedaInformada(self, nodoInicial, algoritmo):
        search = Algoritmos(nodoInicial, algoritmo)             # Variable que usaremos para llamar a los métodos de la clase
        cerrado = set()                                         # Un set es la mejor estructura de datos para los estados ya explorados
        nodosHijo = []                                          # Nodos que se generan cuando expandimos un nodo
        self.nodosGenerados = 1
        self.nodosExpandidos = 0
        estructura = PriorityQueue()                            # Los algoritmos usarán una cola de prioridad
        
        if(algoritmo == 'CosteUniforme'):
            estructura.put((nodoInicial.cost, nodoInicial))         # Si es coste uniforme, nos quedamos con el coste del nodo
        else:
            estructura.put((nodoInicial.heuristic, nodoInicial))    # Si es un algoritmo informado, nos quedamos con la heurística

        while (estructura.qsize() > 0):                             # Comprobamos la cola (qsize), porque peude estar vacía pero "estructura" no lo está, y puede dar error

            nodo = search.removeItem(estructura, algoritmo)         # Sacamos el nodo inicial de la estructura de datos en la que se encuentre
            if(nodo.state not in cerrado):                          # Buscamos si el estado se encuentra explorado
                if(nodo.goalNode()):                                # Comprobamos si el nodo es solución
                    self.m_finalState = nodo.state                  # Nos guardamos el estado final
                    self.finalCost = nodo.cost                      # Nos guardamos el coste final

                    while(nodo.padre != None):                      # Hasta que no lleguemos al nodo inicial, cuyo padre es null, no paramos
                        self.solucion.append(nodo)
                        nodo = nodo.padre

                    self.solucion.append(nodo)                      # Cuando llegamos al padre, lo sacamos a mano
                    print('Algoritmo usado: ', algoritmo)
                    print('Nodos generados: ', self.nodosGenerados)
                    print('Nodos expandidos: ', self.nodosExpandidos)
                    return self.solucion                            # Devolvemos la lista con los nodos solución
                
                self.nodosExpandidos = self.nodosExpandidos + 1
                nodosHijo = self.m_piece.getPossibleActions(nodo.state)    # Depende de la pieza, se almacenan sus posibles movimientos
                self.nodosGenerados = self.nodosGenerados + len(nodosHijo)

                #Aquí estamos iterando posibles movimientos, no estados
                for i in nodosHijo:      
                    # Generamos una copia del nodo actual para no modificarlo
                    nodoCopia = Node(nodo, i, copy.deepcopy(nodo.state, {}).applyAction(i), nodo.cost, (0,0) , search.calculaHeuristica(nodo, algoritmo), nodo.profundidad + 1)   
                    nodoCopia.pos = (nodoCopia.state.m_agentPos.row, nodoCopia.state.m_agentPos.col)                # Actualizamos su posición
                   
                    # Ahora, siguiendo la fórmula para aplicar el coste, actualizamos el coste del nodo
                    nodoCopia.cost = nodoCopia.cost + max(abs(nodo.state.m_agentPos.row - nodoCopia.state.m_agentPos.row), abs(nodo.state.m_agentPos.col - nodoCopia.state.m_agentPos.col)) + 1 
                    nodoCopia.heuristic = search.calculaHeuristica(nodoCopia, algoritmo)                            # Actualizamos la heurística
                    search.insertItem(estructura, algoritmo, nodoCopia, nodoCopia.cost, nodoCopia.heuristic)        # Por último, insertamos el nodo generado en la estructura que le corresponda
                    
                nodosHijo = []              # Vaciamos la lista de nodos hijos para poder utilizarla más tarde
                cerrado.add(nodo.state)     # Insertamos el estado para que no pueda volver a explorarse
        
        return None

    
                                     ################################ Métodos opcionales ################################

    def profundidadLimitada(self, nodoInicial, algoritmo, profundidad):
        cerrado = set()             # Un set es la mejor estructura de datos para los estados ya exploradoss
        nodosHijo = []              # Nodos que se generan cuando expandimos un nodo
        self.nodosGenerados = 1
        self.nodosExpandidos = 0

        estructura = deque()                # AL igual  que búsqueda por profundidad, utilizamos una pila
        estructura.append(nodoInicial)                     

        while (estructura):

            nodo = estructura.pop()                                 # Sacamos el nodo inicial de la estructura de datos en la que se encuentre
            if(nodo.state not in cerrado):                          # Buscamos si el estado se encuentra explorado
                if(nodo.goalNode()):                                # Comprobamos si el nodo es solución
                    self.m_finalState = nodo.state                  # Nos guardamos el estado final
                    self.finalCost = nodo.cost                      # Nos guardamos el coste final

                    while(nodo.padre != None):                      # Hasta que no lleguemos al nodo inicial, cuyo padre es null, no paramos
                        self.solucion.append(nodo)
                        nodo = nodo.padre

                    self.solucion.append(nodo)                      # Cuando llegamos al padre, lo sacamos a mano
                    print('Algoritmo usado: ', algoritmo)
                    print('Nodos generados: ', self.nodosGenerados)
                    print('Nodos expandidos: ', self.nodosExpandidos)
                    print('Profundidad: ', profundidad)
                    return self.solucion                            # Devolvemos la lista con los nodos solución   

                if(nodo.profundidad != profundidad):                            # Si no nos hemos pasado de profundidad, podemos seguir expandiendo
                    self.nodosExpandidos = self.nodosExpandidos + 1
                    nodosHijo = self.m_piece.getPossibleActions(nodo.state)     # Depende de la pieza, se almacenan sus posibles movimientos
                    self.nodosGenerados = self.nodosGenerados + len(nodosHijo)

                    #Aquí estamos iterando posibles movimientos, no estados 
                    for i in nodosHijo:     
                        # Generamos una copia del nodo actual para no modificarlo
                        nodoCopia = Node(nodo, i, copy.deepcopy(nodo.state, {}).applyAction(i), nodo.cost, (0,0) , None, nodo.profundidad + 1)   
                        nodoCopia.pos = (nodoCopia.state.m_agentPos.row, nodoCopia.state.m_agentPos.col)    # Actualizamos su posición

                        # Ahora, siguiendo la fórmula para aplicar el coste, actualizamos el coste del nodo
                        nodoCopia.cost = nodoCopia.cost + max(abs(nodo.state.m_agentPos.row - nodoCopia.state.m_agentPos.row), abs(nodo.state.m_agentPos.col - nodoCopia.state.m_agentPos.col)) + 1
                        estructura.append(nodoCopia)     
                    
                nodosHijo = []              # Vaciamos la lista de nodos hijos para poder utilizarla más tarde
                cerrado.add(nodo.state)     # Insertamos el estado para que no pueda volver a explorarse

        
        return None
        


    def profundidadIterativa(self, nodoInicial, algoritmo, profundidad):
        cerrado = set()             # Un set es la mejor estructura de datos para los estados ya exploradoss
        nodosHijo = []              # Nodos que se generan cuando expandimos un nodo
        self.nodosGenerados = 1
        self.nodosExpandidos = 0

        estructura = deque()                # AL igual  que búsqueda por profundidad, utilizamos una pila
        estructura.append(nodoInicial)
        finales = deque()
        inicial = False                     # Para que no entre en el primer if en el primer nodo      

        while (estructura):
            nodo = estructura.pop()     # Sacamos el nodo inicial de la estructura de datos en la que se encuentre
            
            if (len(estructura) == 0 and inicial):  # Si hemos explorado todo (profundidad limitada), aumentaremos en 1 la profundidad (con el primer nodo no se hace)
                profundidad = profundidad + 1
                estructura = copy.copy(finales)
                finales = deque()
            inicial = True              # A partir de ahora, queremos que se compruebe lo de arriba

            if(nodo.state not in cerrado):                          # Buscamos si el estado se encuentra explorado
                if(nodo.goalNode()):                                # Comprobamos si el nodo es solución
                    self.m_finalState = nodo.state                  # Nos guardamos el estado final
                    self.finalCost = nodo.cost                      # Nos guardamos el coste final

                    while(nodo.padre != None):                      # Hasta que no lleguemos al nodo inicial, cuyo padre es null, no paramos
                        self.solucion.append(nodo)
                        nodo = nodo.padre

                    self.solucion.append(nodo)                      # Cuando llegamos al padre, lo sacamos a mano
                    print('Algoritmo usado: ', algoritmo)
                    print('Nodos generados: ', self.nodosGenerados)
                    print('Nodos expandidos: ', self.nodosExpandidos)
                    print('Profundidad: ', profundidad)
                    return self.solucion                            # Devolvemos la lista con los nodos solución

                if(nodo.profundidad != profundidad):                            # Si no nos hemos pasado de profundidad
                    self.nodosExpandidos = self.nodosExpandidos + 1
                    nodosHijo = self.m_piece.getPossibleActions(nodo.state)     # Depende de la pieza, se almacenan sus posibles movimientos
                    self.nodosGenerados = self.nodosGenerados + len(nodosHijo)

                    #Aquí estamos iterando posibles movimientos, no estados
                    for i in nodosHijo:
                        nodoCopia = Node(nodo, i, copy.deepcopy(nodo.state, {}).applyAction(i) , nodo.cost, (0,0) , None, nodo.profundidad + 1)   # Generamos una copia del nodo actual para no modificarlo
                        nodoCopia.state = nodoCopia.state.applyAction(i)                                    # Le aplicamos la acción
                        nodoCopia.pos = (nodoCopia.state.m_agentPos.row, nodoCopia.state.m_agentPos.col)    # Actualizamos su posición

                        # Ahora, siguiendo la fórmula para aplicar el coste, actualizamos el coste del nodo
                        nodoCopia.cost = nodoCopia.cost + max(abs(nodo.state.m_agentPos.row - nodoCopia.state.m_agentPos.row), abs(nodo.state.m_agentPos.col - nodoCopia.state.m_agentPos.col)) + 1
                        estructura.append(nodoCopia)

                nodosHijo = []              # Vaciamos la lista de nodos hijos para poder utilizarla más tarde

                if(nodo.profundidad < profundidad):
                    cerrado.add(nodo.state)     # Insertamos el estado para que no pueda volver a explorarse
                else:
                    finales.append(nodo)        # Tenemos que aumentar en 1 la profundidad, osea que nos guardamos este nodo

        
        return None




    
