"""
Módulo: Producto
Descripción: Clase que representa un Producto en el inventario
"""


class Producto:
    """
    Representa un producto en el inventario.
    
    Atributos:
        id_producto: Identificador único del producto
        nombre: Nombre del producto
        cantidad: Cantidad en stock
        precio: Precio unitario
        categoria: Categoría del producto
    """
    
    def __init__(self, id_producto, nombre, cantidad, precio, categoria="General"):
        """
        Constructor del producto.
        
        Args:
            id_producto: ID único
            nombre: Nombre del producto
            cantidad: Cantidad inicial
            precio: Precio unitario
            categoria: Categoría (por defecto 'General')
        """
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.categoria = categoria
    
    def obtener_total(self):
        """Calcula el valor total del producto"""
        return self.cantidad * self.precio
    
    def __eq__(self, otro):
        """Compara productos por ID"""
        if isinstance(otro, Producto):
            return self.id_producto == otro.id_producto
        return False
    
    def __repr__(self):
        """Representación en string del producto"""
        return f"Producto(id={self.id_producto}, nombre={self.nombre}, cant={self.cantidad})"
    
    def __str__(self):
        """String amigable del producto"""
        return f"[{self.id_producto}] {self.nombre} - {self.cantidad} unidades @ ${self.precio}"
