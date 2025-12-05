"""
Módulo: Lista Enlazada
Descripción: Implementación de una lista enlazada simple con operaciones básicas
"""

from nodo import Nodo


class ListaEnlazada:
    """
    Implementa una Lista Enlazada Simple.
    
    Una lista enlazada es una estructura de datos donde cada elemento (nodo)
    contiene un dato y una referencia al siguiente nodo.
    
    Ventajas:
        - Inserción/eliminación O(1) si tenemos la referencia
        - Tamaño dinámico
        - No requiere memoria contigua
    
    Desventajas:
        - Acceso O(n) a un elemento arbitrario
        - Requiere más memoria por punteros
    """
    
    def __init__(self):
        """Inicializa una lista enlazada vacía"""
        self.cabeza = None
        self.cola = None
        self.cantidad = 0
    
    def insertar_inicio(self, dato):
        """
        Inserta un elemento al inicio de la lista.
        
        Complejidad: O(1)
        
        Args:
            dato: El valor a insertar
        """
        nuevo_nodo = Nodo(dato)
        
        if self.cabeza is None:
            self.cabeza = self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        
        self.cantidad += 1
    
    def insertar_final(self, dato):
        """
        Inserta un elemento al final de la lista.
        
        Complejidad: O(1) si mantenemos referencia a la cola
        
        Args:
            dato: El valor a insertar
        """
        nuevo_nodo = Nodo(dato)
        
        if self.cabeza is None:
            self.cabeza = self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        
        self.cantidad += 1
    
    def insertar_posicion(self, dato, posicion):
        """
        Inserta un elemento en una posición específica.
        
        Complejidad: O(n) donde n es la posición
        
        Args:
            dato: El valor a insertar
            posicion: La posición donde insertar (0-basada)
            
        Raises:
            ValueError: Si la posición es inválida
        """
        if posicion < 0 or posicion > self.cantidad:
            raise ValueError(f"Posición inválida: {posicion}")
        
        if posicion == 0:
            self.insertar_inicio(dato)
        elif posicion == self.cantidad:
            self.insertar_final(dato)
        else:
            nuevo_nodo = Nodo(dato)
            actual = self._obtener_nodo(posicion - 1)
            nuevo_nodo.siguiente = actual.siguiente
            actual.siguiente = nuevo_nodo
            self.cantidad += 1
    
    def buscar(self, dato):
        """
        Busca un elemento en la lista.
        
        Complejidad: O(n)
        
        Args:
            dato: El valor a buscar
            
        Returns:
            True si encontrado, False en caso contrario
        """
        actual = self.cabeza
        while actual:
            if actual.dato == dato:
                return True
            actual = actual.siguiente
        return False
    
    def buscar_posicion(self, dato):
        """
        Encuentra la posición de un elemento.
        
        Complejidad: O(n)
        
        Args:
            dato: El valor a buscar
            
        Returns:
            La posición si existe, -1 en caso contrario
        """
        actual = self.cabeza
        posicion = 0
        while actual:
            if actual.dato == dato:
                return posicion
            actual = actual.siguiente
            posicion += 1
        return -1
    
    def obtener(self, posicion):
        """
        Obtiene el elemento en una posición específica.
        
        Complejidad: O(n)
        
        Args:
            posicion: La posición del elemento
            
        Returns:
            El dato si existe
            
        Raises:
            IndexError: Si la posición es inválida
        """
        if posicion < 0 or posicion >= self.cantidad:
            raise IndexError("Posición fuera de rango")
        
        return self._obtener_nodo(posicion).dato
    
    def _obtener_nodo(self, posicion):
        """
        Obtiene la referencia al nodo en una posición.
        
        Complejidad: O(n)
        
        Args:
            posicion: La posición del nodo
            
        Returns:
            El nodo en esa posición
        """
        actual = self.cabeza
        for _ in range(posicion):
            actual = actual.siguiente
        return actual
    
    def eliminar(self, dato):
        """
        Elimina la primera ocurrencia de un elemento.
        
        Complejidad: O(n)
        
        Args:
            dato: El valor a eliminar
            
        Returns:
            True si se eliminó, False si no existe
        """
        if self.cabeza is None:
            return False
        
        # Si es la cabeza
        if self.cabeza.dato == dato:
            self.cabeza = self.cabeza.siguiente
            if self.cabeza is None:
                self.cola = None
            self.cantidad -= 1
            return True
        
        # Buscar en el resto
        actual = self.cabeza
        while actual.siguiente:
            if actual.siguiente.dato == dato:
                actual.siguiente = actual.siguiente.siguiente
                if actual.siguiente is None:
                    self.cola = actual
                self.cantidad -= 1
                return True
            actual = actual.siguiente
        
        return False
    
    def eliminar_posicion(self, posicion):
        """
        Elimina el elemento en una posición específica.
        
        Complejidad: O(n)
        
        Args:
            posicion: La posición a eliminar
            
        Returns:
            El dato eliminado
            
        Raises:
            IndexError: Si la posición es inválida
        """
        if posicion < 0 or posicion >= self.cantidad:
            raise IndexError("Posición fuera de rango")
        
        if posicion == 0:
            dato = self.cabeza.dato
            self.cabeza = self.cabeza.siguiente
            if self.cabeza is None:
                self.cola = None
            self.cantidad -= 1
            return dato
        
        anterior = self._obtener_nodo(posicion - 1)
        dato = anterior.siguiente.dato
        anterior.siguiente = anterior.siguiente.siguiente
        if anterior.siguiente is None:
            self.cola = anterior
        self.cantidad -= 1
        return dato
    
    def recorrer(self):
        """
        Retorna todos los elementos de la lista.
        
        Complejidad: O(n)
        
        Returns:
            Lista de Python con todos los datos
        """
        resultado = []
        actual = self.cabeza
        while actual:
            resultado.append(actual.dato)
            actual = actual.siguiente
        return resultado
    
    def esta_vacia(self):
        """
        Verifica si la lista está vacía.
        
        Complejidad: O(1)
        
        Returns:
            True si la lista está vacía
        """
        return self.cantidad == 0
    
    def obtener_cantidad(self):
        """
        Obtiene el número de elementos.
        
        Complejidad: O(1)
        
        Returns:
            Número de elementos
        """
        return self.cantidad
    
    def limpiar(self):
        """
        Limpia toda la lista.
        
        Complejidad: O(1) (las referencias se limpian automáticamente)
        """
        self.cabeza = None
        self.cola = None
        self.cantidad = 0
    
    def __repr__(self):
        """Representación en string de la lista"""
        return f"ListaEnlazada({self.recorrer()})"
    
    def __len__(self):
        """Retorna la cantidad de elementos"""
        return self.cantidad
    
    def __str__(self):
        """Retorna string amigable de la lista"""
        elementos = " -> ".join(str(d) for d in self.recorrer())
        return f"[{elementos}]" if elementos else "[]"
