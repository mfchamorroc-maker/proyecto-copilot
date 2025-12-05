/**
 * Script principal del sistema de gestión de inventario
 * Maneja las interacciones del usuario con la interfaz
 */

// Instancia global del gestor de inventario
let gestor = new GestorInventario();

/**
 * Inicializar la aplicación
 */
document.addEventListener('DOMContentLoaded', function() {
    // Cargar datos de ejemplo
    cargarDatosEjemplo();
    
    // Configurar formulario
    document.getElementById('formularioProducto').addEventListener('submit', function(e) {
        e.preventDefault();
        agregarProductoDesdeFormulario();
    });

    // Mostrar productos iniciales
    mostrarProductos();
});

/**
 * Cargar datos de ejemplo para demostración
 */
function cargarDatosEjemplo() {
    const productos = [
        { nombre: 'Laptop', cantidad: 5, precio: 999.99, categoria: 'Electrónica' },
        { nombre: 'Mouse', cantidad: 20, precio: 29.99, categoria: 'Electrónica' },
        { nombre: 'Teclado', cantidad: 15, precio: 79.99, categoria: 'Electrónica' },
        { nombre: 'Arroz 1kg', cantidad: 50, precio: 2.50, categoria: 'Alimentos' },
        { nombre: 'Frijoles 1kg', cantidad: 30, precio: 3.00, categoria: 'Alimentos' },
        { nombre: 'Camisa', cantidad: 25, precio: 45.00, categoria: 'Ropa' },
        { nombre: 'Pantalón', cantidad: 18, precio: 65.00, categoria: 'Ropa' },
        { nombre: 'JavaScript Básico', cantidad: 8, precio: 29.99, categoria: 'Libros' }
    ];

    for (let producto of productos) {
        gestor.agregarProducto(
            producto.nombre,
            producto.cantidad,
            producto.precio,
            producto.categoria
        );
    }
}

/**
 * Agregar producto desde el formulario
 */
function agregarProductoDesdeFormulario() {
    try {
        const nombre = document.getElementById('nombre').value.trim();
        const cantidad = parseInt(document.getElementById('cantidad').value);
        const precio = parseFloat(document.getElementById('precio').value);
        const categoria = document.getElementById('categoria').value;

        if (!nombre || cantidad < 0 || precio < 0) {
            mostrarAlerta('Por favor completa todos los campos correctamente', 'error');
            return;
        }

        gestor.agregarProducto(nombre, cantidad, precio, categoria);
        mostrarAlerta(`Producto "${nombre}" agregado exitosamente`, 'exito');
        
        // Limpiar formulario
        document.getElementById('formularioProducto').reset();
        
        // Actualizar tabla
        mostrarProductos();
    } catch (error) {
        mostrarAlerta(`Error: ${error.message}`, 'error');
    }
}

/**
 * Mostrar todos los productos en la tabla
 */
function mostrarProductos() {
    const productos = gestor.obtenerTodos();
    const tabla = document.getElementById('tablaProductos');

    if (productos.length === 0) {
        tabla.innerHTML = '<p>No hay productos en el inventario.</p>';
        return;
    }

    let html = `
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Nombre</th>
                    <th>Cantidad</th>
                    <th>Precio</th>
                    <th>Categoría</th>
                    <th>Total</th>
                    <th>Acciones</th>
                </tr>
            </thead>
            <tbody>
    `;

    for (let producto of productos) {
        const total = (producto.cantidad * producto.precio).toFixed(2);
        html += `
            <tr>
                <td>${producto.id}</td>
                <td>${producto.nombre}</td>
                <td>${producto.cantidad}</td>
                <td>$${producto.precio.toFixed(2)}</td>
                <td>${producto.categoria}</td>
                <td>$${total}</td>
                <td>
                    <button class="btn-danger" onclick="eliminarProducto('${producto.id}')">Eliminar</button>
                </td>
            </tr>
        `;
    }

    html += `
            </tbody>
        </table>
    `;

    tabla.innerHTML = html;
}

/**
 * Buscar productos por nombre
 */
function buscarProductos() {
    const termino = document.getElementById('busqueda').value.trim();

    if (!termino) {
        mostrarAlerta('Por favor ingresa un término de búsqueda', 'error');
        return;
    }

    const resultados = gestor.buscarPorNombre(termino);
    const tabla = document.getElementById('tablaProductos');

    if (resultados.length === 0) {
        tabla.innerHTML = `<p>No se encontraron productos que coincidan con "${termino}"</p>`;
        return;
    }

    let html = `
        <h3>Resultados de búsqueda para "${termino}"</h3>
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Nombre</th>
                    <th>Cantidad</th>
                    <th>Precio</th>
                    <th>Categoría</th>
                    <th>Total</th>
                    <th>Acciones</th>
                </tr>
            </thead>
            <tbody>
    `;

    for (let producto of resultados) {
        const total = (producto.cantidad * producto.precio).toFixed(2);
        html += `
            <tr>
                <td>${producto.id}</td>
                <td>${producto.nombre}</td>
                <td>${producto.cantidad}</td>
                <td>$${producto.precio.toFixed(2)}</td>
                <td>${producto.categoria}</td>
                <td>$${total}</td>
                <td>
                    <button class="btn-danger" onclick="eliminarProducto('${producto.id}')">Eliminar</button>
                </td>
            </tr>
        `;
    }

    html += `
            </tbody>
        </table>
        <button class="btn-secondary" onclick="mostrarProductos()">Volver a todos</button>
    `;

    tabla.innerHTML = html;
}

/**
 * Generar reporte del inventario
 */
function generarReporte() {
    const reporte = gestor.generarReporte();
    const div = document.getElementById('reporteResultado');

    let html = `
        <h3>📊 Reporte de Inventario</h3>
        <div class="reporte-stats">
            <div class="stat-card">
                <h4>Total de Productos</h4>
                <div class="valor">${reporte.totalProductos}</div>
            </div>
            <div class="stat-card">
                <h4>Valor Total del Inventario</h4>
                <div class="valor">$${reporte.totalValor}</div>
            </div>
        </div>
    `;

    if (reporte.productosBajo.length > 0) {
        html += `
            <h4>⚠️ Productos con Bajo Stock (< 5 unidades)</h4>
            <ul>
        `;
        for (let producto of reporte.productosBajo) {
            html += `
                <li>${producto.nombre}: ${producto.cantidad} unidades</li>
            `;
        }
        html += `
            </ul>
        `;
    }

    html += `<p><small>Generado: ${reporte.fechaReporte}</small></p>`;

    div.innerHTML = html;
    div.classList.add('activo');
}

/**
 * Eliminar un producto del inventario
 * @param {string} id - ID del producto a eliminar
 */
function eliminarProducto(id) {
    if (confirm('¿Está seguro de que desea eliminar este producto?')) {
        if (gestor.eliminarProducto(id)) {
            mostrarAlerta('Producto eliminado exitosamente', 'exito');
            mostrarProductos();
        } else {
            mostrarAlerta('Error al eliminar el producto', 'error');
        }
    }
}

/**
 * Mostrar alerta temporal
 * @param {string} mensaje - Mensaje a mostrar
 * @param {string} tipo - Tipo de alerta ('exito' o 'error')
 */
function mostrarAlerta(mensaje, tipo) {
    // Crear elemento de alerta
    const alerta = document.createElement('div');
    alerta.className = `alerta ${tipo}`;
    alerta.textContent = mensaje;

    // Insertar al inicio del main
    const main = document.querySelector('main');
    main.insertBefore(alerta, main.firstChild);

    // Remover después de 4 segundos
    setTimeout(() => {
        alerta.remove();
    }, 4000);
}
