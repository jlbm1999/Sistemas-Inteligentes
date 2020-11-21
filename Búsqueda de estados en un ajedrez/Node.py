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
    # De esta manera, se fuerza a que la comparación sea por la y no por el nodo como tal.
    # En el caso del coste uniforme, la variable heurística contiene el coste, por lo que nos sirve también para ese algoritmo.
    def __lt__(self, other):
        return self.heuristic < other.heuristic

    

    

     
     


