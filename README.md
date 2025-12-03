# proyecto-copilot
Proyecto de prueba para Estructura de Datos 2

Blog Técnico: Tablas Hash
Introducción
Colisiones
Operaciones
Bienvenido al Blog sobre Tablas Hash
Explora los conceptos fundamentales, técnicas de manejo de colisiones y operaciones clave de las Tablas Hash.

Introducción a las Tablas Hash
Inicio
¿Qué es una Tabla Hash?
Una Tabla Hash es una estructura de datos que nos permite guardar y buscar información de manera muy rápida. Imagina una caja con muchos compartimentos, donde cada cosa que guardas tiene una etiqueta especial (llamada clave).

Conceptos clave
Clave (key): Es como el nombre o etiqueta que identifica lo que guardas.
Valor (value): Es la información que quieres guardar.
Función hash: Es una fórmula mágica que convierte la clave en un número (índice).
Índice: Es el número que indica en qué compartimento se guarda el valor.
Colisiones: Ocurre cuando dos claves diferentes terminan en el mismo compartimento.
¿Por qué son tan eficientes?
Las tablas hash son muy rápidas porque, usando la función hash, pueden encontrar, agregar o eliminar información casi al instante. En promedio, las operaciones principales (insertar, buscar y eliminar) toman solo un pequeño paso (O(1)).

Ejemplo visual
Arreglo base (Tabla Hash)
key
Función hash
Índice
En el diagrama, la clave pasa por la función hash, que genera un índice para guardar el valor en el arreglo base.

Manejo de Colisiones en Tablas Hash
Inicio
¿Qué es una colisión?
Una colisión ocurre cuando dos claves diferentes terminan en el mismo compartimento de la tabla hash. Es como si dos personas intentaran guardar sus cosas en el mismo cajón.

1. Encadenamiento (Chaining)
En esta técnica, cada compartimento de la tabla puede guardar una lista de valores. Si hay colisión, los valores se agregan a la lista.

Fácil de implementar
Crece dinámicamente
Ejemplo visual: Chaining
Tabla Hash
A
B
C
A
B
En el ejemplo, el compartimento tiene una lista con dos valores (A y B) por colisión.

2. Direccionamiento Abierto (Open Addressing)
En esta técnica, si hay colisión, se busca el siguiente compartimento libre en la tabla. Hay varios métodos:

Linear Probing: Se busca el siguiente espacio disponible uno por uno.
Quadratic Probing: Se salta espacios en forma cuadrática.
Double Hashing: Se usa una segunda función hash para decidir el salto.
Ejemplo visual: Linear Probing
Tabla Hash
A
B
C
En el ejemplo, si el espacio de "A" está ocupado, "B" se coloca en el siguiente espacio disponible.

Implementación y Operaciones Fundamentales
Inicio
Operaciones principales
Insertar (put): Guardar un valor usando una clave.
Buscar (get): Encontrar el valor usando la clave.
Eliminar (delete): Quitar el valor usando la clave.
¿Cómo funciona cada operación?
Insertar (put)
La clave pasa por la función hash, que genera un índice. El valor se guarda en ese lugar. Si hay colisión, se usa la técnica elegida (chaining o open addressing).

// Pseudocódigo sencillo
función insertar(tabla, clave, valor):
    índice = función_hash(clave)
    si tabla[indice] está vacío:
        tabla[indice] = valor
    si no:
        manejar_colisión(tabla, índice, valor)
Buscar (get)
Se calcula el índice con la función hash y se busca el valor en ese lugar. Si hay colisión, se busca en la lista o se sigue la secuencia.

// Pseudocódigo sencillo
función buscar(tabla, clave):
    índice = función_hash(clave)
    si tabla[indice] tiene la clave:
        devolver tabla[indice]
    si no:
        buscar_en_colisión(tabla, índice, clave)
Eliminar (delete)
Se localiza el valor y se elimina. En chaining, se quita de la lista. En open addressing, se marca como "eliminado".

// Pseudocódigo sencillo
función eliminar(tabla, clave):
    índice = función_hash(clave)
    si tabla[indice] tiene la clave:
        quitar tabla[indice]
    si no:
        eliminar_en_colisión(tabla, índice, clave)
Ejemplo visual
Tabla Hash
A
B
C
(vacío)
(eliminado)
Se insertan las claves A, B y C.
Se busca la clave B.
Se elimina la clave en la celda marcada como "eliminado".
