"""
Módulo: Cola (Queue)
Descripción: Implementación de una Cola usando la Lista Enlazada
Una Cola es FIFO (First In, First Out) - el primero en entrar es el primero en salir
"""

from lista_enlazada import ListaEnlazada


class Cola:
    """
    Implementa una Cola (FIFO - First In, First Out).
    
    Una cola es una estructura de datos donde:
    - Los elementos se añaden por el final (encolar)
    - Los elementos se extraen del inicio (desencolar)
    - El primer elemento que entra es el primero que sale
    
    Casos de uso:
        - Procesamiento de tareas
        - Gestión de impresoras
        - Simulación de eventos
        - Atención al cliente
    
    Complejidad de operaciones:
        - Encolar: O(1)
        - Desencolar: O(1)
        - Ver frente: O(1)
        - Buscar: O(n)
    """
    
    def __init__(self):
        """Inicializa una cola vacía"""
        self._lista = ListaEnlazada()
    
    def encolar(self, dato):
        """
        Añade un elemento al final de la cola.
        
        Complejidad: O(1)
        
        Args:
            dato: El valor a encolar
        """
        self._lista.insertar_final(dato)
    
    def desencolar(self):
        """
        Extrae el elemento del inicio de la cola.
        
        Complejidad: O(1)
        
        Returns:
            El primer elemento de la cola
            
        Raises:
            IndexError: Si la cola está vacía
        """
        if self.esta_vacia():
            raise IndexError("Cola vacía")
        
        return self._lista.eliminar_posicion(0)
    
    def frente(self):
        """
        Obtiene el elemento al frente sin extraerlo.
        
        Complejidad: O(1)
        
        Returns:
            El primer elemento de la cola
            
        Raises:
            IndexError: Si la cola está vacía
        """
        if self.esta_vacia():
            raise IndexError("Cola vacía")
        
        return self._lista.obtener(0)
    
    def final(self):
        """
        Obtiene el elemento al final sin extraerlo.
        
        Complejidad: O(1) si mantenemos referencia a la cola
        
        Returns:
            El último elemento de la cola
            
        Raises:
            IndexError: Si la cola está vacía
        """
        if self.esta_vacia():
            raise IndexError("Cola vacía")
        
        return self._lista.obtener(self._lista.obtener_cantidad() - 1)
    
    def esta_vacia(self):
        """
        Verifica si la cola está vacía.
        
        Complejidad: O(1)
        
        Returns:
            True si la cola está vacía
        """
        return self._lista.esta_vacia()
    
    def obtener_cantidad(self):
        """
        Obtiene el número de elementos en la cola.
        
        Complejidad: O(1)
        
        Returns:
            Número de elementos
        """
        return self._lista.obtener_cantidad()
    
    def convertir_a_lista(self):
        """
        Convierte la cola a una lista de Python.
        
        Complejidad: O(n)
        
        Returns:
            Lista con todos los elementos de la cola
        """
        return self._lista.recorrer()
    
    def limpiar(self):
        """
        Limpia toda la cola.
        
        Complejidad: O(1)
        """
        self._lista.limpiar()
    
    def buscar(self, dato):
        """
        Busca un elemento en la cola.
        
        Complejidad: O(n)
        
        Args:
            dato: El valor a buscar
            
        Returns:
            True si existe, False en caso contrario
        """
        return self._lista.buscar(dato)
    
    def __repr__(self):
        """Representación en string de la cola"""
        return f"Cola({self._lista.recorrer()})"
    
    def __len__(self):
        """Retorna la cantidad de elementos"""
        return self.obtener_cantidad()
    
    def __str__(self):
        """Retorna string amigable de la cola"""
        elementos = " <- ".join(str(d) for d in self._lista.recorrer())
        return f"[{elementos}]" if elementos else "[]"
