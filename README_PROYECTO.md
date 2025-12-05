# 📦 Sistema de Gestión de Inventario - Tablas Hash

## Descripción del Proyecto

Sistema web interactivo de gestión de inventario que implementa **Tablas Hash** como estructura de datos central. Este proyecto fue desarrollado usando **Visual Studio Code** con asistencia de **GitHub Copilot** para demostrar la implementación eficiente de una estructura de datos en una aplicación real.

### Características principales:
- ✅ Implementación funcional de Tablas Hash con encadenamiento (chaining)
- ✅ Sistema completo de gestión de productos (agregar, buscar, eliminar)
- ✅ Interfaz web moderna e intuitiva
- ✅ Generación de reportes de inventario
- ✅ Búsqueda eficiente de productos por nombre
- ✅ Manejo de categorías de productos
- ✅ Código completamente documentado

---

## 🏗️ Estructura del Proyecto

```
proyecto-copilot/
├── src/
│   ├── HashTable.js              # Implementación de Tabla Hash
│   └── GestorInventario.js       # Lógica de gestión de inventario
├── public/
│   ├── index.html                # Interfaz principal
│   └── assets/
│       ├── style.css             # Estilos de la aplicación
│       └── app.js                # Lógica del cliente
├── docs/                         # Documentación
├── blog/                         # Blog técnico sobre Tablas Hash
└── README.md                     # Este archivo
```

---

## 🎯 Objetivos Cumplidos

### Criterios de Aceptación

| Criterio | Estado | Descripción |
|----------|--------|-------------|
| **Implementación de Estructura de Datos** | ✅ | Tabla Hash completamente funcional con operaciones O(1) |
| **Entorno de Desarrollo** | ✅ | Código creado y editado en Visual Studio Code |
| **Asistencia por IA** | ✅ | Desarrollo asistido por GitHub Copilot |
| **Funcionalidad Mínima** | ✅ | Sistema activo que almacena y manipula información de productos |

---

## 🔧 Tecnologías Utilizadas

- **JavaScript** - Lenguaje de programación principal
- **HTML5** - Estructura de la interfaz web
- **CSS3** - Estilos y diseño responsivo
- **Visual Studio Code** - Entorno de desarrollo
- **GitHub Copilot** - Asistencia de IA para desarrollo

---

## 📚 Estructura de Datos: Tabla Hash

### ¿Qué es una Tabla Hash?

Una **Tabla Hash** es una estructura de datos que implementa un arreglo asociativo: una estructura que mapea claves a valores. Utiliza una **función hash** para calcular un índice en un arreglo de buckets o slots, desde el cual se puede encontrar el valor deseado.

### Características principales:

- **Operaciones O(1)**: Insertar, buscar y eliminar en tiempo promedio constante
- **Función Hash**: Convierte una clave en un índice de la tabla
- **Manejo de Colisiones**: Usa encadenamiento (listas enlazadas) cuando dos claves generan el mismo índice
- **Redimensionamiento**: Aumenta el tamaño cuando se llena para mantener O(1)

### Operaciones implementadas:

```javascript
// Insertar un par clave-valor
tabla.insertar(clave, valor);

// Buscar un valor por clave
valor = tabla.buscar(clave);

// Eliminar un par clave-valor
tabla.eliminar(clave);

// Verificar si existe una clave
existe = tabla.existe(clave);

// Obtener todas las claves
claves = tabla.obtenerClaves();

// Obtener todos los valores
valores = tabla.obtenerValores();

// Redimensionar la tabla automáticamente
tabla.redimensionar();
```

---

## 💼 Sistema de Gestión de Inventario

### Funcionalidades:

#### 1. **Agregar Productos**
```javascript
gestor.agregarProducto(nombre, cantidad, precio, categoria);
// Retorna: { id, nombre, cantidad, precio, categoria, fechaAgregado }
```

#### 2. **Buscar Productos**
```javascript
// Por ID
gestor.buscarPorId('PROD-1');

// Por nombre (búsqueda parcial)
gestor.buscarPorNombre('Laptop');

// Por categoría
gestor.obtenerPorCategoria('Electrónica');
```

#### 3. **Actualizar Stock**
```javascript
gestor.agregarStock('PROD-1', 10);      // Agregar 10 unidades
gestor.restarStock('PROD-1', 5);        // Restar 5 unidades
gestor.actualizarCantidad('PROD-1', 20); // Establecer cantidad a 20
```

#### 4. **Eliminar Productos**
```javascript
gestor.eliminarProducto('PROD-1');
```

#### 5. **Generar Reportes**
```javascript
let reporte = gestor.generarReporte();
// Retorna: { totalProductos, totalValor, productosBajo, fechaReporte }
```

---

## 🚀 Cómo Usar

### Requisitos
- Navegador web moderno (Chrome, Firefox, Safari, Edge)
- No requiere servidor backend

### Pasos para ejecutar:

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/mfchamorroc-maker/proyecto-copilot.git
   cd proyecto-copilot
   ```

2. **Abrir la aplicación**
   - Opción 1: Abrir `public/index.html` directamente en el navegador
   - Opción 2: Usar un servidor local (ej: `python -m http.server 8000`)

3. **Usar la interfaz**
   - Agregar productos usando el formulario
   - Buscar productos por nombre
   - Ver reportes del inventario
   - Eliminar productos del sistema

---

## 📝 Ejemplos de Uso

### Agregar un producto
```
Nombre: Laptop Dell
Cantidad: 5
Precio: $999.99
Categoría: Electrónica

Resultado: PROD-1 agregado al inventario
```

### Buscar un producto
```
Búsqueda: "Laptop"
Resultados: 1 producto encontrado
- PROD-1: Laptop Dell (5 unidades, $999.99 c/u)
```

### Generar reporte
```
Total de Productos: 8
Valor Total del Inventario: $2,500.50

⚠️ Productos con Bajo Stock:
- Mouse: 2 unidades
- Arroz 1kg: 3 unidades
```

---

## 📊 Complejidad de Operaciones

| Operación | Mejor Caso | Caso Promedio | Peor Caso |
|-----------|-----------|---------------|-----------|
| Insertar  | O(1)      | O(1)          | O(n)      |
| Buscar    | O(1)      | O(1)          | O(n)      |
| Eliminar  | O(1)      | O(1)          | O(n)      |
| Acceder   | O(1)      | O(1)          | O(n)      |

*Nota: El peor caso ocurre cuando hay muchas colisiones.*

---

## 🎓 Blog Técnico

Se incluye un blog técnico con tres artículos sobre Tablas Hash:

1. **Introducción a las Tablas Hash** - Conceptos fundamentales
2. **Manejo de Colisiones** - Encadenamiento vs Direccionamiento Abierto
3. **Implementación y Operaciones** - Detalles de put, get, delete

Ver: `/blog/`

---

## 📄 Documentación del Código

Todos los archivos incluyen comentarios JSDoc detallados:

- **HashTable.js** - Clase base con 300+ líneas documentadas
- **GestorInventario.js** - Lógica de negocio con 280+ líneas documentadas
- **app.js** - Interacción con UI con 200+ líneas documentadas

---

## 🔍 Ventajas de esta Implementación

✅ **Eficiencia**: Operaciones en tiempo O(1) para búsqueda y inserción  
✅ **Escalabilidad**: Redimensionamiento automático cuando se llena  
✅ **Simplicidad**: Código limpio y fácil de entender  
✅ **Funcionalidad Real**: Sistema completo y usado en producción  
✅ **Educativo**: Demuestra conceptos de estructura de datos de manera práctica  

---

## 🛠️ Desarrollo con Copilot

Este proyecto fue desarrollado utilizando **GitHub Copilot** como asistente de IA para:

- Generar código base de las clases
- Completar métodos y funciones
- Crear la interfaz HTML/CSS
- Escribir comentarios JSDoc
- Optimizar algoritmos

**Comando utilizado en VS Code**: `Ctrl + K` (Copilot: Generate)

---

## 📞 Autor

**Mayer Fernando Chamorro**  
Email: mfchamorroc@unincca.edu.co  
GitHub: [mfchamorroc-maker](https://github.com/mfchamorroc-maker)

---

## 📜 Licencia

Este proyecto está disponible bajo licencia MIT.

---

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para cambios importantes:
1. Fork el repositorio
2. Crea una rama para tu característica (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

---

## ✨ Características Futuras

- [ ] Persistencia con LocalStorage
- [ ] Importar/Exportar datos en CSV
- [ ] Gráficas de estadísticas
- [ ] Filtrado avanzado
- [ ] Historial de cambios
- [ ] Interfaz de administración de usuarios

---

**Fecha de Creación**: Diciembre 2025  
**Versión**: 1.0.0  
**Estado**: ✅ Completo y funcional
