/**
 * Clase HashTable - Implementación de Tabla Hash con Encadenamiento (Chaining)
 * 
 * Esta clase implementa una tabla hash utilizando arreglos para almacenar pares clave-valor.
 * Cuando ocurren colisiones, se utiliza la técnica de encadenamiento (listas enlazadas).
 */

class HashTable {
    /**
     * Constructor - Inicializa la tabla hash
     * @param {number} tamaño - Tamaño inicial de la tabla (por defecto 50)
     */
    constructor(tamaño = 50) {
        this.tamaño = tamaño;
        this.tabla = new Array(tamaño).fill(null).map(() => []);
        this.cantidad = 0;
    }

    /**
     * Función hash - Convierte una clave en un índice
     * @param {string} clave - La clave a hash
     * @returns {number} Índice dentro del rango de la tabla
     */
    funcionHash(clave) {
        let hash = 0;
        for (let i = 0; i < clave.length; i++) {
            hash += clave.charCodeAt(i);
        }
        return hash % this.tamaño;
    }

    /**
     * Insertar - Agrega un par clave-valor a la tabla
     * Si la clave ya existe, actualiza el valor
     * @param {string} clave - La clave
     * @param {*} valor - El valor a guardar
     */
    insertar(clave, valor) {
        const indice = this.funcionHash(clave);
        const bucket = this.tabla[indice];

        // Buscar si la clave ya existe
        for (let i = 0; i < bucket.length; i++) {
            if (bucket[i].clave === clave) {
                bucket[i].valor = valor; // Actualizar valor
                return;
            }
        }

        // Si no existe, agregar nuevo par
        bucket.push({ clave, valor });
        this.cantidad++;

        // Redimensionar si es necesario
        if (this.cantidad / this.tamaño > 0.75) {
            this.redimensionar();
        }
    }

    /**
     * Buscar - Obtiene el valor asociado a una clave
     * @param {string} clave - La clave a buscar
     * @returns {*} El valor si existe, undefined si no
     */
    buscar(clave) {
        const indice = this.funcionHash(clave);
        const bucket = this.tabla[indice];

        for (let i = 0; i < bucket.length; i++) {
            if (bucket[i].clave === clave) {
                return bucket[i].valor;
            }
        }
        return undefined;
    }

    /**
     * Eliminar - Remueve un par clave-valor de la tabla
     * @param {string} clave - La clave a eliminar
     * @returns {boolean} true si se eliminó, false si no existía
     */
    eliminar(clave) {
        const indice = this.funcionHash(clave);
        const bucket = this.tabla[indice];

        for (let i = 0; i < bucket.length; i++) {
            if (bucket[i].clave === clave) {
                bucket.splice(i, 1);
                this.cantidad--;
                return true;
            }
        }
        return false;
    }

    /**
     * Redimensionar - Aumenta el tamaño de la tabla cuando se llena
     * Redistribuye todos los elementos en los nuevos buckets
     */
    redimensionar() {
        const tablaAnterior = this.tabla;
        this.tamaño = Math.floor(this.tamaño * 2);
        this.tabla = new Array(this.tamaño).fill(null).map(() => []);
        this.cantidad = 0;

        // Reinsertar todos los elementos
        for (let bucket of tablaAnterior) {
            for (let item of bucket) {
                this.insertar(item.clave, item.valor);
            }
        }
    }

    /**
     * Obtener todas las claves
     * @returns {array} Array con todas las claves
     */
    obtenerClaves() {
        const claves = [];
        for (let bucket of this.tabla) {
            for (let item of bucket) {
                claves.push(item.clave);
            }
        }
        return claves;
    }

    /**
     * Obtener todos los valores
     * @returns {array} Array con todos los valores
     */
    obtenerValores() {
        const valores = [];
        for (let bucket of this.tabla) {
            for (let item of bucket) {
                valores.push(item.valor);
            }
        }
        return valores;
    }

    /**
     * Obtener todos los pares clave-valor
     * @returns {array} Array de objetos {clave, valor}
     */
    obtenerTodos() {
        const todos = [];
        for (let bucket of this.tabla) {
            for (let item of bucket) {
                todos.push({ clave: item.clave, valor: item.valor });
            }
        }
        return todos;
    }

    /**
     * Verificar si existe una clave
     * @param {string} clave - La clave a verificar
     * @returns {boolean} true si existe, false en caso contrario
     */
    existe(clave) {
        return this.buscar(clave) !== undefined;
    }

    /**
     * Obtener el número de elementos
     * @returns {number} Cantidad de elementos en la tabla
     */
    obtenerCantidad() {
        return this.cantidad;
    }

    /**
     * Limpiar la tabla
     */
    limpiar() {
        this.tabla = new Array(this.tamaño).fill(null).map(() => []);
        this.cantidad = 0;
    }
}

// Exportar para usar en otros módulos
if (typeof module !== 'undefined' && module.exports) {
    module.exports = HashTable;
}
