"""
Módulo: Pruebas Unitarias
Descripción: Pruebas para las estructuras de datos y el gestor de inventario
"""

import sys
import os

# Agregar src al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from lista_enlazada import ListaEnlazada
from cola import Cola
from producto import Producto
from gestor_inventario import GestorInventario


def test_lista_enlazada():
    """Pruebas para ListaEnlazada"""
    print("=" * 50)
    print("PRUEBAS: LISTA ENLAZADA")
    print("=" * 50)
    
    lista = ListaEnlazada()
    
    # Test 1: Insertar al inicio
    print("\n1. Insertar al inicio: 10, 20, 30")
    lista.insertar_inicio(10)
    lista.insertar_inicio(20)
    lista.insertar_inicio(30)
    print(f"   Lista: {lista}")
    assert lista.recorrer() == [30, 20, 10], "Error en insertar_inicio"
    
    # Test 2: Insertar al final
    print("\n2. Insertar al final: 5")
    lista.insertar_final(5)
    print(f"   Lista: {lista}")
    assert lista.recorrer() == [30, 20, 10, 5], "Error en insertar_final"
    
    # Test 3: Buscar
    print("\n3. Buscar elemento 20")
    resultado = lista.buscar(20)
    print(f"   Encontrado: {resultado}")
    assert resultado == True, "Error en buscar"
    
    # Test 4: Eliminar
    print("\n4. Eliminar elemento 20")
    lista.eliminar(20)
    print(f"   Lista: {lista}")
    assert lista.recorrer() == [30, 10, 5], "Error en eliminar"
    
    # Test 5: Cantidad
    print(f"\n5. Cantidad de elementos: {len(lista)}")
    assert len(lista) == 3, "Error en cantidad"
    
    print("\n✅ Todos los tests de ListaEnlazada pasaron\n")


def test_cola():
    """Pruebas para Cola"""
    print("=" * 50)
    print("PRUEBAS: COLA (FIFO)")
    print("=" * 50)
    
    cola = Cola()
    
    # Test 1: Encolar
    print("\n1. Encolar: 100, 200, 300")
    cola.encolar(100)
    cola.encolar(200)
    cola.encolar(300)
    print(f"   Cola: {cola}")
    assert cola.obtener_cantidad() == 3, "Error en encolar"
    
    # Test 2: Ver frente
    print(f"\n2. Frente de la cola: {cola.frente()}")
    assert cola.frente() == 100, "Error en frente"
    
    # Test 3: Desencolar
    print("\n3. Desencolar")
    primer = cola.desencolar()
    print(f"   Elemento descolado: {primer}")
    print(f"   Cola después: {cola}")
    assert primer == 100, "Error en desencolar"
    assert cola.obtener_cantidad() == 2, "Error en cantidad después de desencolar"
    
    # Test 4: FIFO
    print("\n4. Verificar FIFO (First In, First Out)")
    cola.encolar(400)
    elementos = [cola.desencolar() for _ in range(3)]
    print(f"   Orden de salida: {elementos}")
    assert elementos == [200, 300, 400], "Error en FIFO"
    
    print("\n✅ Todos los tests de Cola pasaron\n")


def test_gestor_inventario():
    """Pruebas para GestorInventario"""
    print("=" * 50)
    print("PRUEBAS: GESTOR DE INVENTARIO")
    print("=" * 50)
    
    gestor = GestorInventario()
    
    # Test 1: Agregar productos
    print("\n1. Agregar productos")
    p1 = gestor.agregar_producto("Laptop", 5, 999.99, "Electrónica")
    p2 = gestor.agregar_producto("Mouse", 20, 29.99, "Electrónica")
    p3 = gestor.agregar_producto("Arroz", 50, 2.50, "Alimentos")
    print(f"   Productos agregados: {gestor.obtener_cantidad_total()}")
    assert gestor.obtener_cantidad_total() == 3, "Error en cantidad de productos"
    
    # Test 2: Buscar producto
    print("\n2. Buscar producto por ID")
    encontrado = gestor.buscar_producto_por_id(p1.id_producto)
    print(f"   Encontrado: {encontrado}")
    assert encontrado is not None, "Error al buscar producto"
    
    # Test 3: Buscar por nombre
    print("\n3. Buscar productos por nombre 'Laptop'")
    resultados = gestor.buscar_productos_por_nombre("Laptop")
    print(f"   Resultados: {len(resultados)}")
    assert len(resultados) == 1, "Error en búsqueda por nombre"
    
    # Test 4: Actualizar stock
    print("\n4. Reducir stock de Laptop (5 → 3)")
    original = p1.cantidad
    nueva = gestor.restar_stock(p1.id_producto, 2)
    print(f"   Stock anterior: {original}, Stock nuevo: {nueva}")
    assert nueva == 3, "Error al restar stock"
    
    # Test 5: Crear orden de venta
    print("\n5. Crear orden de venta (COLA FIFO)")
    productos_orden = [(p1.id_producto, 2), (p2.id_producto, 5)]
    orden1 = gestor.crear_orden_venta("CLIENTE-001", productos_orden)
    print(f"   Orden creada - Total: ${orden1['total']}")
    print(f"   Órdenes pendientes: {gestor.obtener_cantidad_ordenes_pendientes()}")
    
    # Test 6: Procesar orden
    print("\n6. Procesar orden (desencolar de cola)")
    orden_procesada = gestor.procesar_proximo_orden()
    print(f"   Orden procesada - Estado: {orden_procesada['estado']}")
    assert orden_procesada['estado'] == "Procesada", "Error al procesar orden"
    
    # Test 7: Generar reporte
    print("\n7. Generar reporte")
    reporte = gestor.generar_reporte()
    print(f"   Total de productos: {reporte['total_productos']}")
    print(f"   Valor total inventario: ${reporte['total_valor_inventario']}")
    print(f"   Órdenes procesadas: {reporte['ordenes_procesadas']}")
    
    print("\n✅ Todos los tests de GestorInventario pasaron\n")


def test_integracion():
    """Test de integración completa"""
    print("=" * 50)
    print("TEST DE INTEGRACIÓN")
    print("=" * 50)
    
    gestor = GestorInventario()
    
    # Agregar varios productos
    print("\n1. Agregando múltiples productos...")
    for i in range(5):
        gestor.agregar_producto(f"Producto {i+1}", 10 + i*5, 10 + i, "Categoría A")
    
    print(f"   Total de productos: {gestor.obtener_cantidad_total()}")
    
    # Crear múltiples órdenes
    print("\n2. Creando órdenes (se encolan en la cola)...")
    productos_disp = gestor.obtener_todos_productos()
    
    for cliente_id in range(1, 4):
        productos_orden = [(productos_disp[cliente_id-1].id_producto, 2)]
        gestor.crear_orden_venta(f"CLIENTE-{cliente_id:03d}", productos_orden)
    
    print(f"   Órdenes pendientes en cola: {gestor.obtener_cantidad_ordenes_pendientes()}")
    
    # Procesar órdenes (FIFO)
    print("\n3. Procesando órdenes (FIFO)...")
    while gestor.obtener_cantidad_ordenes_pendientes() > 0:
        orden = gestor.procesar_proximo_orden()
        print(f"   Procesada orden de {orden['id_cliente']}")
    
    print(f"   Órdenes procesadas en total: {len(gestor.ordenes_procesadas)}")
    
    # Generar reporte final
    print("\n4. Reporte final:")
    reporte = gestor.generar_reporte()
    for clave, valor in reporte.items():
        if clave != "productos_bajo_stock":
            print(f"   {clave}: {valor}")
    
    print("\n✅ Test de integración completado\n")


if __name__ == "__main__":
    try:
        test_lista_enlazada()
        test_cola()
        test_gestor_inventario()
        test_integracion()
        
        print("=" * 50)
        print("🎉 TODOS LOS TESTS PASARON CORRECTAMENTE")
        print("=" * 50)
    except AssertionError as e:
        print(f"\n❌ Error en test: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
        sys.exit(1)
