# Sistema de Gestión de Inventario - Python (Listas y Colas)

## 📋 Descripción

Sistema completo de gestión de inventario implementado en **Python** usando **Listas Enlazadas** y **Colas (FIFO)** como estructuras de datos principales.

### Características:
- ✅ Lista Enlazada para almacenar productos
- ✅ Cola FIFO para procesamiento de órdenes de venta
- ✅ API REST con Flask
- ✅ Búsqueda, inserción y eliminación eficiente
- ✅ Generación de reportes
- ✅ Tests unitarios completos

---

## 📁 Estructura del Proyecto

```
python/
├── src/
│   ├── nodo.py                  # Clase Nodo para listas enlazadas
│   ├── lista_enlazada.py        # Clase ListaEnlazada
│   ├── cola.py                  # Clase Cola (FIFO)
│   ├── producto.py              # Clase Producto
│   └── gestor_inventario.py    # Gestor principal
├── tests/
│   └── test_estructuras.py      # Tests unitarios
├── app.py                       # API REST con Flask
├── requirements.txt             # Dependencias
└── README.md                    # Este archivo
```

---

## 🏗️ Estructuras de Datos Implementadas

### 1. Lista Enlazada
- Almacena productos en una lista dinámica
- Operaciones:
  - `insertar_inicio()` - O(1)
  - `insertar_final()` - O(1)
  - `buscar()` - O(n)
  - `eliminar()` - O(n)
  - `recorrer()` - O(n)

### 2. Cola (FIFO)
- Procesa órdenes de venta en orden de llegada
- Operaciones:
  - `encolar()` - O(1)
  - `desencolar()` - O(1)
  - `frente()` - O(1)
  - `esta_vacia()` - O(1)

---

## 🚀 Instalación y Uso

### 1. Instalar dependencias
```bash
cd python
pip install -r requirements.txt
```

### 2. Ejecutar tests
```bash
python tests/test_estructuras.py
```

Salida esperada:
```
==================================================
PRUEBAS: LISTA ENLAZADA
==================================================

1. Insertar al inicio: 10, 20, 30
   Lista: [30 -> 20 -> 10]

2. Insertar al final: 5
   Lista: [30 -> 20 -> 10 -> 5]

...

🎉 TODOS LOS TESTS PASARON CORRECTAMENTE
```

### 3. Ejecutar servidor API
```bash
python app.py
```

El servidor estará disponible en: `http://localhost:5000`

---

## 📚 Clases Principales

### Nodo
```python
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
```

### ListaEnlazada
```python
lista = ListaEnlazada()
lista.insertar_final(10)
lista.insertar_final(20)
lista.buscar(10)          # True
lista.eliminar(10)
print(lista.recorrer())   # [20]
```

### Cola
```python
cola = Cola()
cola.encolar(1)           # Añade al final
cola.encolar(2)
cola.desencolar()         # Extrae del inicio (retorna 1) - FIFO
cola.frente()             # Mira el primero (retorna 2)
```

### GestorInventario
```python
gestor = GestorInventario()

# Agregar productos
p1 = gestor.agregar_producto("Laptop", 5, 999.99, "Electrónica")

# Buscar
producto = gestor.buscar_producto_por_id("PROD-1")

# Crear orden (se encola)
gestor.crear_orden_venta("CLIENTE-1", [("PROD-1", 2)])

# Procesar orden (desencola)
orden = gestor.procesar_proximo_orden()

# Generar reporte
reporte = gestor.generar_reporte()
```

---

## 🔌 API REST Endpoints

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/api/productos` | Obtener todos los productos |
| GET | `/api/productos/<id>` | Obtener un producto |
| POST | `/api/productos` | Crear nuevo producto |
| DELETE | `/api/productos/<id>` | Eliminar producto |
| PUT | `/api/productos/<id>/cantidad` | Actualizar cantidad |
| GET | `/api/productos/buscar/<nombre>` | Buscar por nombre |
| GET | `/api/ordenes` | Obtener órdenes procesadas |
| POST | `/api/ordenes` | Crear nueva orden |
| POST | `/api/ordenes/procesar` | Procesar siguiente orden (desencolar) |
| GET | `/api/ordenes/pendiente` | Ver siguiente orden sin procesar |
| GET | `/api/reporte` | Generar reporte |

---

## 💻 Ejemplos de Uso

### Ejemplo 1: Agregar y buscar productos
```python
from src.gestor_inventario import GestorInventario

gestor = GestorInventario()

# Agregar productos
gestor.agregar_producto("Laptop", 5, 999.99, "Electrónica")
gestor.agregar_producto("Mouse", 20, 29.99, "Electrónica")

# Buscar
laptops = gestor.buscar_productos_por_nombre("Laptop")
print(laptops)  # Devuelve lista de productos que coinciden
```

### Ejemplo 2: Procesar órdenes con Cola FIFO
```python
# Crear varias órdenes (se encolan)
gestor.crear_orden_venta("CLIENTE-1", [("PROD-1", 2)])
gestor.crear_orden_venta("CLIENTE-2", [("PROD-2", 3)])
gestor.crear_orden_venta("CLIENTE-3", [("PROD-3", 1)])

# Procesar en orden FIFO
print(f"Órdenes pendientes: {gestor.obtener_cantidad_ordenes_pendientes()}")

# Desencolar y procesar
while gestor.obtener_cantidad_ordenes_pendientes() > 0:
    orden = gestor.procesar_proximo_orden()
    print(f"Procesada orden de {orden['id_cliente']}")
```

### Ejemplo 3: Generar reportes
```python
reporte = gestor.generar_reporte()

print(f"Total de productos: {reporte['total_productos']}")
print(f"Valor total: ${reporte['total_valor_inventario']}")
print(f"Órdenes procesadas: {reporte['ordenes_procesadas']}")
print(f"Órdenes pendientes: {reporte['ordenes_pendientes']}")

# Ver productos con bajo stock
for p in reporte['productos_bajo_stock']:
    print(f"⚠️  {p.nombre}: {p.cantidad} unidades")
```

---

## 📊 Complejidad de Operaciones

### ListaEnlazada
| Operación | Complejidad | Notas |
|-----------|------------|-------|
| Insertar inicio | O(1) | Acceso directo a cabeza |
| Insertar final | O(1) | Si mantenemos ref. a cola |
| Insertar posición i | O(i) | Requiere recorrer |
| Buscar | O(n) | Búsqueda lineal |
| Eliminar | O(n) | Requiere buscar primero |
| Recorrer | O(n) | Visitar cada nodo |

### Cola
| Operación | Complejidad |
|-----------|------------|
| Encolar | O(1) |
| Desencolar | O(1) |
| Ver frente | O(1) |
| Buscar | O(n) |

### GestorInventario
| Operación | Complejidad |
|-----------|------------|
| Agregar producto | O(1) |
| Buscar por ID | O(n) |
| Buscar por nombre | O(n) |
| Crear orden | O(n) - n productos en orden |
| Procesar orden | O(1) |

---

## 🧪 Tests

Ejecutar tests:
```bash
python tests/test_estructuras.py
```

Tests incluidos:
- ✅ Inserción en lista enlazada
- ✅ Eliminación de elementos
- ✅ Búsqueda
- ✅ Operaciones FIFO en cola
- ✅ Creación y procesamiento de órdenes
- ✅ Generación de reportes
- ✅ Test de integración completo

---

## 🔐 Manejo de Errores

El sistema incluye validación para:
- Cantidades negativas
- Productos inexistentes
- Stock insuficiente
- Colas vacías
- Datos inválidos

```python
try:
    gestor.restar_stock("PROD-1", 100)
except ValueError as e:
    print(f"Error: {e}")  # Stock insuficiente...
```

---

## 📈 Ventajas de esta Implementación

✅ **Eficiente**: Operaciones O(1) para datos críticos  
✅ **Escalable**: Listas dinámicas sin límite de tamaño  
✅ **Ordenado**: FIFO para procesar órdenes de forma justa  
✅ **Flexible**: Fácil de modificar y extender  
✅ **Educativo**: Código limpio y bien documentado  
✅ **Testeable**: Incluye tests unitarios completos  

---

## 🎓 Conceptos Educativos

Este proyecto demuestra:
- Estructuras de datos enlazadas
- Implementación de colas FIFO
- Complejidad algorítmica
- Diseño orientado a objetos
- API REST
- Tests unitarios en Python

---

## 📝 Autor

**Mayer Fernando Chamorro**  
Estructura de Datos - UNINCCA  
Diciembre 2025

---

## 📄 Licencia

MIT License

---

**¿Necesitas ayuda?** Revisa los tests o ejecuta `python app.py` para ver el API en acción.
