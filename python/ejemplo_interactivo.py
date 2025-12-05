"""
Módulo: Ejemplo Interactivo
Descripción: Demostración interactiva del sistema de inventario
"""

import sys
import os

# Agregar src al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from gestor_inventario import GestorInventario


def mostrar_menu():
    """Muestra el menú principal"""
    print("\n" + "="*60)
    print("SISTEMA DE GESTIÓN DE INVENTARIO - PYTHON")
    print("Usando: Listas Enlazadas + Colas (FIFO)")
    print("="*60)
    print("\n📦 GESTIÓN DE PRODUCTOS:")
    print("  1. Agregar producto")
    print("  2. Ver todos los productos")
    print("  3. Buscar producto por nombre")
    print("  4. Actualizar stock")
    print("  5. Eliminar producto")
    print("\n📋 GESTIÓN DE ÓRDENES:")
    print("  6. Crear orden de venta")
    print("  7. Ver próxima orden pendiente")
    print("  8. Procesar siguiente orden (FIFO)")
    print("  9. Ver órdenes procesadas")
    print("\n📊 REPORTES:")
    print(" 10. Generar reporte")
    print("\n0. Salir")
    print("-"*60)


def mostrar_productos(productos):
    """Muestra la lista de productos"""
    if not productos:
        print("❌ No hay productos en el inventario")
        return
    
    print("\n" + "-"*80)
    print(f"{'ID':<10} {'Nombre':<20} {'Cantidad':<10} {'Precio':<12} {'Total':<15}")
    print("-"*80)
    
    for p in productos:
        total = p.obtener_total()
        print(f"{p.id_producto:<10} {p.nombre:<20} {p.cantidad:<10} ${p.precio:<11.2f} ${total:<14.2f}")
    
    print("-"*80)


def main():
    """Función principal"""
    gestor = GestorInventario()
    
    # Cargar datos de ejemplo
    print("\n⏳ Cargando datos de ejemplo...")
    gestor.agregar_producto("Laptop", 5, 999.99, "Electrónica")
    gestor.agregar_producto("Mouse", 20, 29.99, "Electrónica")
    gestor.agregar_producto("Teclado", 15, 79.99, "Electrónica")
    gestor.agregar_producto("Arroz 1kg", 50, 2.50, "Alimentos")
    gestor.agregar_producto("Frijoles 1kg", 30, 3.00, "Alimentos")
    gestor.agregar_producto("Camisa", 25, 45.00, "Ropa")
    print("✅ Datos de ejemplo cargados\n")
    
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ").strip()
        
        # GESTIÓN DE PRODUCTOS
        if opcion == "1":
            print("\n--- Agregar Producto ---")
            nombre = input("Nombre: ").strip()
            try:
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                categoria = input("Categoría (default: General): ").strip() or "General"
                
                producto = gestor.agregar_producto(nombre, cantidad, precio, categoria)
                print(f"✅ Producto agregado: {producto}")
            except ValueError:
                print("❌ Error: Ingresa valores numéricos válidos")
        
        elif opcion == "2":
            print("\n--- Todos los Productos ---")
            mostrar_productos(gestor.obtener_todos_productos())
        
        elif opcion == "3":
            print("\n--- Buscar Producto ---")
            nombre = input("Nombre a buscar: ").strip()
            resultados = gestor.buscar_productos_por_nombre(nombre)
            
            if resultados:
                print(f"\n✅ Se encontraron {len(resultados)} resultado(s):")
                mostrar_productos(resultados)
            else:
                print("❌ No se encontraron productos")
        
        elif opcion == "4":
            print("\n--- Actualizar Stock ---")
            id_prod = input("ID del producto: ").strip()
            try:
                nueva_cant = int(input("Nueva cantidad: "))
                if gestor.actualizar_cantidad(id_prod, nueva_cant):
                    print("✅ Stock actualizado")
                else:
                    print("❌ Producto no encontrado")
            except ValueError:
                print("❌ Error: Ingresa un número válido")
        
        elif opcion == "5":
            print("\n--- Eliminar Producto ---")
            id_prod = input("ID del producto a eliminar: ").strip()
            if gestor.eliminar_producto(id_prod):
                print("✅ Producto eliminado")
            else:
                print("❌ Producto no encontrado")
        
        # GESTIÓN DE ÓRDENES
        elif opcion == "6":
            print("\n--- Crear Orden de Venta ---")
            id_cliente = input("ID del cliente: ").strip()
            
            productos_orden = []
            while True:
                id_prod = input("ID del producto (o 'listo' para terminar): ").strip()
                if id_prod.lower() == "listo":
                    break
                
                try:
                    cantidad = int(input(f"  Cantidad de {id_prod}: "))
                    productos_orden.append((id_prod, cantidad))
                except ValueError:
                    print("❌ Error: Ingresa cantidad válida")
            
            if productos_orden:
                try:
                    orden = gestor.crear_orden_venta(id_cliente, productos_orden)
                    print(f"\n✅ Orden creada - Total: ${orden['total']:.2f}")
                except ValueError as e:
                    print(f"❌ Error: {e}")
            else:
                print("❌ No se agregaron productos a la orden")
        
        elif opcion == "7":
            print("\n--- Próxima Orden Pendiente ---")
            orden = gestor.obtener_proximo_orden()
            
            if orden:
                print(f"\nCliente: {orden['id_cliente']}")
                print(f"Estado: {orden['estado']}")
                print(f"Total: ${orden['total']:.2f}")
                print(f"Productos:")
                for prod in orden['productos']:
                    print(f"  - {prod['nombre']}: {prod['cantidad']} x ${prod['precio_unitario']:.2f}")
            else:
                print("❌ No hay órdenes pendientes")
        
        elif opcion == "8":
            print("\n--- Procesar Siguiente Orden (FIFO) ---")
            orden = gestor.procesar_proximo_orden()
            
            if orden:
                print(f"✅ Orden procesada")
                print(f"Cliente: {orden['id_cliente']}")
                print(f"Total: ${orden['total']:.2f}")
            else:
                print("❌ No hay órdenes pendientes para procesar")
        
        elif opcion == "9":
            print("\n--- Órdenes Procesadas ---")
            if gestor.ordenes_procesadas:
                for i, orden in enumerate(gestor.ordenes_procesadas, 1):
                    print(f"\n{i}. Cliente: {orden['id_cliente']} | Total: ${orden['total']:.2f}")
            else:
                print("❌ No hay órdenes procesadas")
        
        # REPORTES
        elif opcion == "10":
            print("\n--- Reporte del Inventario ---")
            reporte = gestor.generar_reporte()
            
            print(f"\n📊 ESTADÍSTICAS:")
            print(f"   Total de productos: {reporte['total_productos']}")
            print(f"   Valor total del inventario: ${reporte['total_valor_inventario']:.2f}")
            print(f"   Órdenes procesadas: {reporte['ordenes_procesadas']}")
            print(f"   Órdenes pendientes en cola: {reporte['ordenes_pendientes']}")
            
            if reporte['productos_bajo_stock']:
                print(f"\n⚠️  PRODUCTOS CON BAJO STOCK (< 5 unidades):")
                for p in reporte['productos_bajo_stock']:
                    print(f"   - {p.nombre}: {p.cantidad} unidades")
            else:
                print(f"\n✅ Todos los productos tienen stock adecuado")
        
        elif opcion == "0":
            print("\n👋 ¡Hasta luego!")
            break
        
        else:
            print("❌ Opción inválida. Intenta nuevamente.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Programa interrumpido por el usuario")
    except Exception as e:
        print(f"\n❌ Error: {e}")
