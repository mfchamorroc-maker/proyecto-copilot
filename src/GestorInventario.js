/**
 * Clase GestorInventario - Gestiona productos usando HashTable
 * 
 * Proporciona funcionalidades para:
 * - Agregar productos al inventario
 * - Buscar productos por código o nombre
 * - Actualizar cantidad de stock
 * - Eliminar productos
 * - Generar reportes del inventario
 */

class GestorInventario {
    /**
     * Constructor - Inicializa el gestor de inventario
     */
    constructor() {
        this.inventario = new HashTable();
        this.proximoId = 1;
    }

    /**
     * Agregar un nuevo producto al inventario
     * @param {string} nombre - Nombre del producto
     * @param {number} cantidad - Cantidad en stock
     * @param {number} precio - Precio unitario
     * @param {string} categoria - Categoría del producto
     * @returns {object} Objeto producto creado
     */
    agregarProducto(nombre, cantidad, precio, categoria = 'General') {
        if (!nombre || cantidad < 0 || precio < 0) {
            throw new Error('Datos inválidos: verifica nombre, cantidad y precio');
        }

        const id = `PROD-${this.proximoId}`;
        this.proximoId++;

        const producto = {
            id,
            nombre,
            cantidad,
            precio,
            categoria,
            fechaAgregado: new Date().toLocaleDateString()
        };

        this.inventario.insertar(id, producto);
        return producto;
    }

    /**
     * Buscar producto por ID
     * @param {string} id - ID del producto
     * @returns {object} Objeto producto o null
     */
    buscarPorId(id) {
        return this.inventario.buscar(id) || null;
    }

    /**
     * Buscar productos por nombre (búsqueda parcial)
     * @param {string} nombre - Nombre o parte del nombre
     * @returns {array} Array de productos que coinciden
     */
    buscarPorNombre(nombre) {
        const resultados = [];
        const productos = this.inventario.obtenerTodos();
        
        for (let item of productos) {
            if (item.valor.nombre.toLowerCase().includes(nombre.toLowerCase())) {
                resultados.push(item.valor);
            }
        }
        return resultados;
    }

    /**
     * Actualizar cantidad de un producto
     * @param {string} id - ID del producto
     * @param {number} nuevaCantidad - Nueva cantidad
     * @returns {boolean} true si se actualizó, false si no existe
     */
    actualizarCantidad(id, nuevaCantidad) {
        const producto = this.inventario.buscar(id);
        if (!producto) return false;

        producto.cantidad = nuevaCantidad;
        this.inventario.insertar(id, producto);
        return true;
    }

    /**
     * Aumentar cantidad de un producto
     * @param {string} id - ID del producto
     * @param {number} cantidad - Cantidad a agregar
     * @returns {number} Nueva cantidad o -1 si error
     */
    agregarStock(id, cantidad) {
        const producto = this.inventario.buscar(id);
        if (!producto) return -1;

        producto.cantidad += cantidad;
        this.inventario.insertar(id, producto);
        return producto.cantidad;
    }

    /**
     * Reducir cantidad de un producto
     * @param {string} id - ID del producto
     * @param {number} cantidad - Cantidad a restar
     * @returns {number} Nueva cantidad o -1 si error
     */
    restarStock(id, cantidad) {
        const producto = this.inventario.buscar(id);
        if (!producto) return -1;

        if (producto.cantidad < cantidad) {
            throw new Error('Stock insuficiente');
        }

        producto.cantidad -= cantidad;
        this.inventario.insertar(id, producto);
        return producto.cantidad;
    }

    /**
     * Eliminar un producto del inventario
     * @param {string} id - ID del producto
     * @returns {boolean} true si se eliminó, false si no existe
     */
    eliminarProducto(id) {
        return this.inventario.eliminar(id);
    }

    /**
     * Obtener todos los productos
     * @returns {array} Array de productos
     */
    obtenerTodos() {
        const todos = this.inventario.obtenerTodos();
        return todos.map(item => item.valor);
    }

    /**
     * Obtener productos por categoría
     * @param {string} categoria - Categoría a filtrar
     * @returns {array} Array de productos de esa categoría
     */
    obtenerPorCategoria(categoria) {
        const productos = this.obtenerTodos();
        return productos.filter(p => p.categoria === categoria);
    }

    /**
     * Generar reporte del inventario
     * @returns {object} Reporte con estadísticas
     */
    generarReporte() {
        const productos = this.obtenerTodos();
        let totalProductos = productos.length;
        let totalValor = 0;
        let productosBajo = [];

        for (let producto of productos) {
            totalValor += producto.cantidad * producto.precio;
            if (producto.cantidad < 5) {
                productosBajo.push(producto);
            }
        }

        return {
            totalProductos,
            totalValor: totalValor.toFixed(2),
            productosBajo,
            fechaReporte: new Date().toLocaleString()
        };
    }

    /**
     * Obtener cantidad total de productos en inventario
     * @returns {number} Cantidad de registros
     */
    obtenerCantidad() {
        return this.inventario.obtenerCantidad();
    }

    /**
     * Limpiar todo el inventario
     */
    limpiar() {
        this.inventario.limpiar();
        this.proximoId = 1;
    }
}

// Exportar para usar en otros módulos
if (typeof module !== 'undefined' && module.exports) {
    module.exports = GestorInventario;
}
