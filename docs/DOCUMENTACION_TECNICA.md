# 📖 Documentación Técnica - Sistema de Gestión de Inventario

## Tabla de Contenidos

1. [Arquitectura del Sistema](#arquitectura-del-sistema)
2. [Clase HashTable](#clase-hashtable)
3. [Clase GestorInventario](#clase-gestorinventario)
4. [Interfaz Web](#interfaz-web)
5. [Flujo de Datos](#flujo-de-datos)
6. [Ejemplos de Código](#ejemplos-de-código)

---

## Arquitectura del Sistema

```
┌─────────────────────────────────────────────┐
│         Interfaz Web (HTML/CSS/JS)          │
├─────────────────────────────────────────────┤
│    GestorInventario (Lógica de Negocio)    │
├─────────────────────────────────────────────┤
│      HashTable (Estructura de Datos)        │
└─────────────────────────────────────────────┘
```

### Capas:

1. **Presentación**: HTML/CSS/JS en `public/`
   - Formularios para entrada de datos
   - Tablas para visualización
   - Reportes interactivos

2. **Lógica**: GestorInventario en `src/`
   - Validación de datos
   - Operaciones de negocio
   - Generación de reportes

3. **Datos**: HashTable en `src/`
   - Almacenamiento eficiente
   - Búsqueda rápida
   - Gestión de colisiones

---

## Clase HashTable

### Propiedades

```javascript
class HashTable {
    tamaño: number           // Tamaño actual de la tabla
    tabla: array[][]         // Arreglo de buckets (listas)
    cantidad: number         // Número de elementos almacenados
}
```

### Métodos Principales

#### `constructor(tamaño = 50)`
- Inicializa la tabla hash con un tamaño específico
- Crea buckets vacíos para encadenamiento

#### `funcionHash(clave: string): number`
- Convierte una clave en un índice válido
- Suma códigos ASCII y aplica módulo

```javascript
// Ejemplo:
// clave: "PROD-1" → hash = 32 (índice 32 % 50)
```

#### `insertar(clave, valor)`
- Agrega un nuevo par clave-valor
- Actualiza si la clave ya existe
- Redimensiona automáticamente si es necesario

```javascript
// Proceso:
1. Calcular hash(clave)
2. Buscar en bucket[índice]
3. Si existe → actualizar
4. Si no existe → agregar
5. Si carga > 75% → redimensionar
```

#### `buscar(clave): valor`
- Busca un valor por su clave
- Retorna `undefined` si no existe

```javascript
// Complejidad promedio: O(1)
// Peor caso: O(n) si hay muchas colisiones
```

#### `eliminar(clave): boolean`
- Elimina un par clave-valor
- Retorna `true` si se eliminó

#### `redimensionar()`
- Duplica el tamaño de la tabla
- Redistribuye todos los elementos
- Minimiza colisiones

---

## Clase GestorInventario

### Propiedades

```javascript
class GestorInventario {
    inventario: HashTable    // Tabla hash de productos
    proximoId: number        // Contador para generar IDs
}
```

### Estructura de un Producto

```javascript
{
    id: string,              // "PROD-1", "PROD-2", etc.
    nombre: string,          // Nombre del producto
    cantidad: number,        // Stock disponible
    precio: number,          // Precio unitario
    categoria: string,       // Categoría de clasificación
    fechaAgregado: string    // Fecha de ingreso
}
```

### Métodos Principales

#### `agregarProducto(nombre, cantidad, precio, categoria)`
- Crea un nuevo producto con ID único
- Valida que los datos sean correctos
- Lo almacena en la HashTable

```javascript
// Ejemplo:
const producto = gestor.agregarProducto(
    "Laptop",
    5,
    999.99,
    "Electrónica"
);
// Retorna: { id: "PROD-1", nombre: "Laptop", ... }
```

#### `buscarPorId(id): producto`
- Búsqueda O(1) usando la HashTable
- Retorna el producto o null

#### `buscarPorNombre(nombre): array`
- Búsqueda lineal entre todos los productos
- Búsqueda parcial (case-insensitive)

```javascript
// Ejemplo:
gestor.buscarPorNombre("Lap");
// Retorna: [{ Laptop }, { Laptop Gamer }]
```

#### `agregarStock(id, cantidad): number`
- Aumenta el stock de un producto
- Retorna la nueva cantidad

#### `restarStock(id, cantidad): number`
- Disminuye el stock de un producto
- Lanza error si no hay suficiente stock

#### `generarReporte(): object`
- Calcula estadísticas del inventario

```javascript
{
    totalProductos: 8,
    totalValor: "2500.50",
    productosBajo: [
        { id: "PROD-2", nombre: "Mouse", cantidad: 2 }
    ],
    fechaReporte: "4/12/2025, 14:30:45"
}
```

---

## Interfaz Web

### Componentes Principales

#### 1. Formulario de Productos
- Campo: Nombre del producto
- Campo: Cantidad
- Campo: Precio unitario
- Selector: Categoría
- Botón: Agregar Producto

#### 2. Tabla de Productos
- Columnas: ID, Nombre, Cantidad, Precio, Categoría, Total, Acciones
- Búsqueda interactiva
- Eliminación directa desde la tabla

#### 3. Buscador
- Input para buscar por nombre
- Búsqueda en tiempo real
- Opción para volver a la vista completa

#### 4. Reportes
- Botón para generar reporte
- Estadísticas: Total de productos, Valor total
- Alertas: Productos con bajo stock

#### 5. Sistema de Alertas
- Notificaciones de éxito/error
- Desaparecen automáticamente en 4 segundos

---

## Flujo de Datos

### Agregar un Producto

```
Usuario llena formulario
        ↓
Evento submit capturado
        ↓
Validación de datos
        ↓
gestor.agregarProducto()
        ↓
GestorInventario valida
        ↓
HashTable.insertar(id, producto)
        ↓
Se calcula hash(id)
        ↓
Producto se agrega al bucket[indice]
        ↓
Interfaz se actualiza con mostrarProductos()
        ↓
Usuario ve nuevo producto en la tabla
```

### Buscar un Producto

```
Usuario escribe nombre y hace clic en Buscar
        ↓
gestor.buscarPorNombre(termino)
        ↓
Itera sobre todos los productos
        ↓
Filtra por coincidencias (case-insensitive)
        ↓
Retorna array de resultados
        ↓
Interface muestra resultados en tabla
```

---

## Ejemplos de Código

### Ejemplo 1: Crear y usar la HashTable

```javascript
// Crear tabla hash
const tabla = new HashTable(50);

// Insertar pares clave-valor
tabla.insertar("usuario1", { nombre: "Juan", edad: 25 });
tabla.insertar("usuario2", { nombre: "María", edad: 30 });

// Buscar
let usuario = tabla.buscar("usuario1");
console.log(usuario); // { nombre: "Juan", edad: 25 }

// Verificar existencia
if (tabla.existe("usuario1")) {
    console.log("Usuario existe");
}

// Eliminar
tabla.eliminar("usuario2");
```

### Ejemplo 2: Usar el GestorInventario

```javascript
// Crear gestor
const gestor = new GestorInventario();

// Agregar productos
gestor.agregarProducto("Mouse", 20, 29.99, "Electrónica");
gestor.agregarProducto("Teclado", 15, 79.99, "Electrónica");

// Buscar
const productos = gestor.buscarPorNombre("Mouse");

// Actualizar stock
gestor.agregarStock("PROD-1", 10);
gestor.restarStock("PROD-1", 5);

// Ver todos
const todos = gestor.obtenerTodos();

// Generar reporte
const reporte = gestor.generarReporte();
console.log(`Total de productos: ${reporte.totalProductos}`);
console.log(`Valor total: $${reporte.totalValor}`);
```

### Ejemplo 3: Manejo de Colisiones

```javascript
// La tabla hash maneja automáticamente las colisiones
const tabla = new HashTable(5); // Tabla pequeña (fuerza colisiones)

tabla.insertar("apple", 100);
tabla.insertar("apply", 200);  // Posible colisión
tabla.insertar("append", 300); // Posible colisión

// Todos se almacenan correctamente en buckets de listas
console.log(tabla.buscar("apple"));  // 100
console.log(tabla.buscar("apply"));  // 200
console.log(tabla.buscar("append")); // 300
```

---

## Ventajas de la Implementación

### Eficiencia
- Búsqueda O(1) en promedio
- Inserción O(1) en promedio
- Eliminación O(1) en promedio

### Escalabilidad
- Redimensionamiento automático
- Factor de carga controlado (75%)
- Adaptable a cualquier cantidad de datos

### Confiabilidad
- Manejo de colisiones con encadenamiento
- Validación de datos en cada operación
- Recuperación de errores

### Usabilidad
- Interfaz intuitiva y responsiva
- Mensajes de error claros
- Datos de ejemplo precargados

---

## Casos de Uso

1. **Gestión de Inventario Pequeño-Mediano**: Tiendas, almacenes
2. **Sistema de Usuarios**: Autenticación y perfiles
3. **Caché de datos**: Almacenamiento temporal rápido
4. **Indexación de Documentos**: Búsqueda eficiente

---

## Limitaciones y Mejoras Futuras

### Limitaciones Actuales
- Datos se pierden al recargar la página
- No hay persistencia en base de datos
- No hay autenticación de usuarios
- Búsqueda solo por nombre exacta/parcial

### Mejoras Propuestas
- Integración con LocalStorage o Firebase
- API REST backend
- Autenticación y roles de usuario
- Búsqueda avanzada con filtros complejos
- Exportación a CSV/PDF
- Gráficas de estadísticas

---

**Última actualización**: Diciembre 2025  
**Versión**: 1.0.0
