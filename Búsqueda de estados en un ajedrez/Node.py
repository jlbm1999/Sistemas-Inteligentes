# Clase en la que se modelarán los nodos del grafo

import copy

class Node:

    # __slots__ = (self.cost, Node)

    def __init__(self, padre, accion, state, cost, pos, heuristic, profundidad):
        self.padre = padre
        self.accion = accion
        self.state = state
        self.cost = cost
        self.pos = pos
        self.heuristic = heuristic
        self.profundidad = profundidad

    def goalNode(self):
        if(self.state.isFinal()): return True
    
    # Puesto que la cola de prioridad no permite comparar nodos como tal, necesitamos este método.
    # De esta manera, se fuerza a que la comparación sea por el coste y no por el nodo como tal.
    def __lt__(self, other):
        if((self.heuristic == None) or (other.heuristic == None)):  # Si la heurística de algún nodo es None, es no informada
            if(self.cost < other.cost):
                return self.cost < other.cost 
        else:
            return self.heuristic < other.heuristic

    

    

     
     


