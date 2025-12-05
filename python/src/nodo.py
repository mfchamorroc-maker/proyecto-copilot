"""
Módulo: Nodo
Descripción: Clase base para un nodo en una estructura de datos enlazada
"""


class Nodo:
    """
    Representa un nodo en una lista enlazada.
    
    Atributos:
        dato: El valor almacenado en el nodo
        siguiente: Referencia al siguiente nodo (None si es el último)
    """
    
    def __init__(self, dato):
        """
        Constructor del nodo.
        
        Args:
            dato: El valor a almacenar en el nodo
        """
        self.dato = dato
        self.siguiente = None
    
    def __repr__(self):
        """Representación en string del nodo"""
        return f"Nodo({self.dato})"
