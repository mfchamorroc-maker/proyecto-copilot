"""
Módulo: Gestor de Inventario
Descripción: Sistema de gestión de inventario usando Listas Enlazadas y Colas
"""

from lista_enlazada import ListaEnlazada
from cola import Cola
from producto import Producto


class GestorInventario:
    """
    Gestor de Inventario usando Estructuras de Datos:
    - Lista Enlazada: Para almacenar productos
    - Cola: Para manejar órdenes/solicitudes de venta
    
    Funcionalidades:
        - Agregar productos
        - Buscar productos
        - Actualizar stock
        - Eliminar productos
        - Procesar órdenes de venta (FIFO)
        - Generar reportes
    """
    
    def __init__(self):
        """Inicializa el gestor de inventario"""
        self.productos = ListaEnlazada()  # Lista enlazada de productos
        self.ordenes_venta = Cola()       # Cola de órdenes de venta
        self.proximo_id = 1
        self.ordenes_procesadas = []
    
    def agregar_producto(self, nombre, cantidad, precio, categoria="General"):
        """
        Agrega un nuevo producto al inventario.
        
        Complejidad: O(1)
        
        Args:
            nombre: Nombre del producto
            cantidad: Cantidad en stock
            precio: Precio unitario
            categoria: Categoría del producto
            
        Returns:
            El producto creado
        """
        if cantidad < 0 or precio < 0:
            raise ValueError("Cantidad y precio deben ser positivos")
        
        id_prod = f"PROD-{self.proximo_id}"
        self.proximo_id += 1
        
        producto = Producto(id_prod, nombre, cantidad, precio, categoria)
        self.productos.insertar_final(producto)
        
        return producto
    
    def buscar_producto_por_id(self, id_producto):
        """
        Busca un producto por su ID.
        
        Complejidad: O(n)
        
        Args:
            id_producto: ID del producto
            
        Returns:
            El producto si existe, None en caso contrario
        """
        lista_productos = self.productos.recorrer()
        for producto in lista_productos:
            if producto.id_producto == id_producto:
                return producto
        return None
    
    def buscar_productos_por_nombre(self, nombre):
        """
        Busca productos por nombre (búsqueda parcial).
        
        Complejidad: O(n)
        
        Args:
            nombre: Nombre o parte del nombre
            
        Returns:
            Lista de productos que coinciden
        """
        resultados = []
        lista_productos = self.productos.recorrer()
        
        for producto in lista_productos:
            if nombre.lower() in producto.nombre.lower():
                resultados.append(producto)
        
        return resultados
    
    def actualizar_cantidad(self, id_producto, nueva_cantidad):
        """
        Actualiza la cantidad de un producto.
        
        Complejidad: O(n)
        
        Args:
            id_producto: ID del producto
            nueva_cantidad: Nueva cantidad
            
        Returns:
            True si se actualizó, False si no existe
        """
        producto = self.buscar_producto_por_id(id_producto)
        
        if producto is None:
            return False
        
        if nueva_cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        
        producto.cantidad = nueva_cantidad
        return True
    
    def agregar_stock(self, id_producto, cantidad):
        """
        Aumenta el stock de un producto.
        
        Complejidad: O(n)
        
        Args:
            id_producto: ID del producto
            cantidad: Cantidad a agregar
            
        Returns:
            Nueva cantidad o -1 si error
        """
        producto = self.buscar_producto_por_id(id_producto)
        
        if producto is None:
            return -1
        
        if cantidad < 0:
            raise ValueError("Cantidad debe ser positiva")
        
        producto.cantidad += cantidad
        return producto.cantidad
    
    def restar_stock(self, id_producto, cantidad):
        """
        Disminuye el stock de un producto.
        
        Complejidad: O(n)
        
        Args:
            id_producto: ID del producto
            cantidad: Cantidad a restar
            
        Returns:
            Nueva cantidad o -1 si error
            
        Raises:
            ValueError: Si no hay suficiente stock
        """
        producto = self.buscar_producto_por_id(id_producto)
        
        if producto is None:
            return -1
        
        if cantidad < 0:
            raise ValueError("Cantidad debe ser positiva")
        
        if producto.cantidad < cantidad:
            raise ValueError(f"Stock insuficiente. Disponible: {producto.cantidad}")
        
        producto.cantidad -= cantidad
        return producto.cantidad
    
    def eliminar_producto(self, id_producto):
        """
        Elimina un producto del inventario.
        
        Complejidad: O(n)
        
        Args:
            id_producto: ID del producto
            
        Returns:
            True si se eliminó, False si no existe
        """
        producto = self.buscar_producto_por_id(id_producto)
        
        if producto is None:
            return False
        
        return self.productos.eliminar(producto)
    
    def obtener_todos_productos(self):
        """
        Obtiene todos los productos.
        
        Complejidad: O(n)
        
        Returns:
            Lista de todos los productos
        """
        return self.productos.recorrer()
    
    def obtener_productos_por_categoria(self, categoria):
        """
        Obtiene productos filtrados por categoría.
        
        Complejidad: O(n)
        
        Args:
            categoria: Categoría a filtrar
            
        Returns:
            Lista de productos de esa categoría
        """
        resultados = []
        lista_productos = self.productos.recorrer()
        
        for producto in lista_productos:
            if producto.categoria == categoria:
                resultados.append(producto)
        
        return resultados
    
    def crear_orden_venta(self, id_cliente, productos_solicitados):
        """
        Crea una orden de venta y la añade a la cola de órdenes.
        
        Complejidad: O(n) - n es la cantidad de productos en la orden
        
        Args:
            id_cliente: ID del cliente
            productos_solicitados: Lista de tuplas (id_producto, cantidad)
            
        Returns:
            La orden creada o None si hay error
        """
        orden = {
            "id_cliente": id_cliente,
            "productos": [],
            "total": 0,
            "estado": "Pendiente"
        }
        
        for id_prod, cantidad in productos_solicitados:
            producto = self.buscar_producto_por_id(id_prod)
            
            if producto is None:
                raise ValueError(f"Producto {id_prod} no existe")
            
            if producto.cantidad < cantidad:
                raise ValueError(f"Stock insuficiente de {producto.nombre}")
            
            orden["productos"].append({
                "id_producto": id_prod,
                "nombre": producto.nombre,
                "cantidad": cantidad,
                "precio_unitario": producto.precio,
                "subtotal": cantidad * producto.precio
            })
            
            orden["total"] += cantidad * producto.precio
            producto.cantidad -= cantidad
        
        self.ordenes_venta.encolar(orden)
        return orden
    
    def procesar_proximo_orden(self):
        """
        Procesa el siguiente orden de venta de la cola (FIFO).
        
        Complejidad: O(1) para desencolar
        
        Returns:
            La orden procesada o None si no hay órdenes
        """
        if self.ordenes_venta.esta_vacia():
            return None
        
        orden = self.ordenes_venta.desencolar()
        orden["estado"] = "Procesada"
        self.ordenes_procesadas.append(orden)
        
        return orden
    
    def obtener_proximo_orden(self):
        """
        Obtiene el próximo orden sin procesarlo.
        
        Complejidad: O(1)
        
        Returns:
            El próximo orden o None si no hay
        """
        if self.ordenes_venta.esta_vacia():
            return None
        
        return self.ordenes_venta.frente()
    
    def obtener_cantidad_ordenes_pendientes(self):
        """
        Obtiene la cantidad de órdenes pendientes.
        
        Complejidad: O(1)
        
        Returns:
            Número de órdenes en cola
        """
        return self.ordenes_venta.obtener_cantidad()
    
    def generar_reporte(self):
        """
        Genera un reporte del inventario.
        
        Complejidad: O(n)
        
        Returns:
            Diccionario con estadísticas
        """
        productos = self.obtener_todos_productos()
        
        total_productos = len(productos)
        total_valor = sum(p.obtener_total() for p in productos)
        productos_bajo_stock = [p for p in productos if p.cantidad < 5]
        
        return {
            "total_productos": total_productos,
            "total_valor_inventario": round(total_valor, 2),
            "productos_bajo_stock": productos_bajo_stock,
            "ordenes_procesadas": len(self.ordenes_procesadas),
            "ordenes_pendientes": self.obtener_cantidad_ordenes_pendientes()
        }
    
    def obtener_cantidad_total(self):
        """
        Obtiene la cantidad total de productos únicos en inventario.
        
        Complejidad: O(1)
        
        Returns:
            Número de productos
        """
        return self.productos.obtener_cantidad()
    
    def limpiar(self):
        """
        Limpia todo el inventario.
        
        Complejidad: O(1)
        """
        self.productos.limpiar()
        self.ordenes_venta.limpiar()
        self.ordenes_procesadas.clear()
        self.proximo_id = 1
