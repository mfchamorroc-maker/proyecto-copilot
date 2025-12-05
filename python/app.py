"""
Módulo: API REST Flask
Descripción: API para el Sistema de Gestión de Inventario
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os

# Agregar src al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from gestor_inventario import GestorInventario

app = Flask(__name__)
CORS(app)

# Instancia global del gestor
gestor = GestorInventario()

# Cargar datos de ejemplo
def cargar_datos_ejemplo():
    """Carga datos de ejemplo para demostración"""
    gestor.agregar_producto("Laptop", 5, 999.99, "Electrónica")
    gestor.agregar_producto("Mouse", 20, 29.99, "Electrónica")
    gestor.agregar_producto("Teclado", 15, 79.99, "Electrónica")
    gestor.agregar_producto("Arroz 1kg", 50, 2.50, "Alimentos")
    gestor.agregar_producto("Frijoles 1kg", 30, 3.00, "Alimentos")
    gestor.agregar_producto("Camisa", 25, 45.00, "Ropa")
    gestor.agregar_producto("Pantalón", 18, 65.00, "Ropa")
    gestor.agregar_producto("JavaScript Básico", 8, 29.99, "Libros")

# API Endpoints

@app.route('/api/saludo', methods=['GET'])
def saludo():
    """Endpoint de prueba"""
    return jsonify({"mensaje": "API de Gestión de Inventario funcionando"})

@app.route('/api/productos', methods=['GET'])
def obtener_productos():
    """Obtiene todos los productos"""
    productos = gestor.obtener_todos_productos()
    productos_dict = [
        {
            "id": p.id_producto,
            "nombre": p.nombre,
            "cantidad": p.cantidad,
            "precio": p.precio,
            "categoria": p.categoria,
            "total": p.obtener_total()
        }
        for p in productos
    ]
    return jsonify(productos_dict)

@app.route('/api/productos/<id_producto>', methods=['GET'])
def obtener_producto(id_producto):
    """Obtiene un producto específico"""
    producto = gestor.buscar_producto_por_id(id_producto)
    
    if producto is None:
        return jsonify({"error": "Producto no encontrado"}), 404
    
    return jsonify({
        "id": producto.id_producto,
        "nombre": producto.nombre,
        "cantidad": producto.cantidad,
        "precio": producto.precio,
        "categoria": producto.categoria,
        "total": producto.obtener_total()
    })

@app.route('/api/productos', methods=['POST'])
def crear_producto():
    """Crea un nuevo producto"""
    data = request.get_json()
    
    try:
        producto = gestor.agregar_producto(
            data.get("nombre"),
            data.get("cantidad", 0),
            data.get("precio", 0),
            data.get("categoria", "General")
        )
        
        return jsonify({
            "id": producto.id_producto,
            "nombre": producto.nombre,
            "cantidad": producto.cantidad,
            "precio": producto.precio,
            "categoria": producto.categoria
        }), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/productos/<id_producto>', methods=['DELETE'])
def eliminar_producto(id_producto):
    """Elimina un producto"""
    if gestor.eliminar_producto(id_producto):
        return jsonify({"mensaje": "Producto eliminado"}), 200
    else:
        return jsonify({"error": "Producto no encontrado"}), 404

@app.route('/api/productos/<id_producto>/cantidad', methods=['PUT'])
def actualizar_cantidad(id_producto):
    """Actualiza la cantidad de un producto"""
    data = request.get_json()
    nueva_cantidad = data.get("cantidad")
    
    if nueva_cantidad is None:
        return jsonify({"error": "Cantidad no especificada"}), 400
    
    if gestor.actualizar_cantidad(id_producto, nueva_cantidad):
        return jsonify({"mensaje": "Cantidad actualizada"}), 200
    else:
        return jsonify({"error": "Producto no encontrado"}), 404

@app.route('/api/productos/buscar/<nombre>', methods=['GET'])
def buscar_productos(nombre):
    """Busca productos por nombre"""
    productos = gestor.buscar_productos_por_nombre(nombre)
    productos_dict = [
        {
            "id": p.id_producto,
            "nombre": p.nombre,
            "cantidad": p.cantidad,
            "precio": p.precio,
            "categoria": p.categoria
        }
        for p in productos
    ]
    return jsonify(productos_dict)

@app.route('/api/ordenes', methods=['GET'])
def obtener_ordenes():
    """Obtiene las órdenes procesadas"""
    return jsonify(gestor.ordenes_procesadas)

@app.route('/api/ordenes', methods=['POST'])
def crear_orden():
    """Crea una nueva orden de venta"""
    data = request.get_json()
    
    try:
        orden = gestor.crear_orden_venta(
            data.get("id_cliente"),
            data.get("productos", [])
        )
        return jsonify(orden), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/ordenes/procesar', methods=['POST'])
def procesar_orden():
    """Procesa el siguiente orden de la cola"""
    orden = gestor.procesar_proximo_orden()
    
    if orden is None:
        return jsonify({"error": "No hay órdenes pendientes"}), 404
    
    return jsonify(orden), 200

@app.route('/api/ordenes/pendiente', methods=['GET'])
def obtener_proximo_orden():
    """Obtiene el próximo orden sin procesarlo"""
    orden = gestor.obtener_proximo_orden()
    
    if orden is None:
        return jsonify({"mensaje": "No hay órdenes pendientes"}), 404
    
    return jsonify(orden)

@app.route('/api/reporte', methods=['GET'])
def obtener_reporte():
    """Obtiene el reporte del inventario"""
    reporte = gestor.generar_reporte()
    
    # Convertir productos a diccionarios
    productos_bajo_stock = [
        {
            "id": p.id_producto,
            "nombre": p.nombre,
            "cantidad": p.cantidad
        }
        for p in reporte["productos_bajo_stock"]
    ]
    
    reporte["productos_bajo_stock"] = productos_bajo_stock
    
    return jsonify(reporte)

@app.errorhandler(404)
def no_encontrado(error):
    """Manejador de rutas no encontradas"""
    return jsonify({"error": "Ruta no encontrada"}), 404

@app.errorhandler(500)
def error_servidor(error):
    """Manejador de errores del servidor"""
    return jsonify({"error": "Error interno del servidor"}), 500

if __name__ == '__main__':
    cargar_datos_ejemplo()
    app.run(debug=True, port=5000, host='0.0.0.0')
