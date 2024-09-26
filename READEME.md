# Estructuras de Datos Lineales con Python

Curso para implementar python, terminal para resolucion de problemas.

Se recomienda saber:
a. Pensamiento Logico y Algoritmos
b. Terminal y linea de comandos
c. Curso de POO
d. Curso de Introducción al Pensamiento Computacional con Python

## Objejtivo

a. Entender el concepto e importancia de estructuras de datos
b. Comprender el compprtamiento, uso e implementacion de datos lineales con python
c. Poner en practica lo aprendido

## Por que python?

Estructuras de datos con Python ayuda a reducir la complejidad y facilita su entendimiento.
Python tiene las siguientes ventajasÑ
a. sintaxis clara y simple
b. semantica segura
c. escalable
d. interactivo
e. proposito general
f. gratis y popular

Brilla mas para inteligencia de datas, data science y backend.

## Contenido del curso

a. Introduccion
b. Elementos en Python
c. Colecciones
d. Tipos y operaciones

## Estructuras de datos lineales

a. Arrays
b. Nodes
c. LInked Lists
d. Stacks
e. Queues

# Elementos de programacion e n Python

a. elementos lexicos
. if, while, def, etc

b. convenciones
. variable, constante, nombre_funcion, nombreClase

c. tomar en cuenta
. sintaxis
. lietrales
. operadores
. import
. condicionales
. loops

## estructruras propias

a. listas
b. tuplas
c. conjunots (sets)
d. diccionarios

## funciones

a. declaraciones y llmada
b. recursivas
c. anidadas
d. high order functions
e. lambdas

## ademas

a. manejo de excepciones y errores
b. manipulacion de archivos

# Tipos de colecciones

Nos referimos tambien a las estructuras de datos.

## que es una coleccion?

Es un grupo de cero o mas elementos que pueden tratarse como una unidad conceptual.

En la programacion los datos pueden tener distintas representaciones, unos son datos iguales a cero o no cero. Como un numero negativo.

Tambien hay datos como null o non en python, siginifca nada, otro tipo de dato es undefined, cuando no se define que tipo de dato es.

Pueden formar parte o no de una coleccion.

## Tipos de colecciones

a. Dinamicas
b. Inmutables: no cambiaran su tamano, ni crecer ni reducirse.

### Lineales

a. Ordenadas por posicion
b. Solo el primer elemento NO tiene predecesor.
c. Todas tienen un predecesor, excepto primera o la ultima.
d. si es dinamica esta puede crecer y el ultimo elemento puede tener sucesores

Ejemplos:

a. Fila en el supermercado
b. Pila de platos
c. Checklist de tareas

### Jerariquicas

a. Ordenadas como un arbol invertido
b. Solo el primer elemento no tiene predecesores, pero si tiene sucesores
c. COn padres e hijos
d. tiene n sucesores

Ejemplos:
a. sistema de directorios, no tienen limite excepto el limite en memoria de la computadora.
b. indices de libros, con capitulos, temas y subtemas, etc.

### Grafos

a. Cada dato puede tener varios predecesores y sucesores
b. como no son jerarquitcos, tienen veciones

ejemplo:

a. rutas de los vuelos que pueden estar conectados a varios destinos o a ninguno

### Desordenadas

a. No tienen orden particular.
b. No hay predecesores o sucesores.

Los elementos simplemente estan ahi.

Ejemplo:
a. Canicas
b. Premios de loteria cuando estan representados con esferas

### Ordenadas

a. impone un orden con una regla como

item < item+1

que le dara orden

ejemplo:
a. como un calogo de pintura

### Taxonomia de estructuras de datos.

a. Nos concentraremos en las lineales en este curso.

### El eterno dilema

Al buscar en estructuras de bases de datos, tenemos que balancear entre poco costo de recursos y la velocidad.
Pero las estructuras de datos, al ser colecciones con caracteristicas especificas no spermiten que bajo ciertas circunstancias tengan un desempeno mayor.

Son herramientas y segun el caso de uso, son las estructuras a usar. veremos cuales son.

# Stack vs Queue

Habla sobre la eficiencia que se puede obtener en memoria y velocidad cuando se utilizan las estructuras de datos aporpiadas, en este caso el Queue puede ser mas rapidas para operaciones como agregar y eleimnar que los stacks.

# Operaciones esenciales en colecciones

## Operaciones

a. Tamanio
b. Pertenencia: si se encuentra dentro de una coleccion
c. Recorrido: para recorrer la coleccion, sobre cada uno de sus elementos
d. String: convertir a string
e. Igualdad: saber si la coleccion es igual a otra o alguno de sus elementos.
f. Concatenacion
g. Conversion de tipo: de un tipo de dato a otro
h. Insertar: al principio al final o en una posicion determinada
i. Remover: al principio al final o en una posicion determinada
j. Reemplazar: tomar un elemento de la coleccion, eliminarlo y poner otro
k. Acceder: a uno o todos los elemntos de la coleccion

# Colecciones incorporadas

## Listas

a. Propostio general.
b. Estructura mas utilizada.
c. Tamanio dinamico.
d. De tipo secuencial con un indice.
e. Ordenable.

```py
# Formas para construir listas

list1 = list()
list2 = ['t', 25, 'cat', 3.1416]
list3 = list[number**2 for number in range(1, 100, 3)]

print(list1)
print(list2)
print(list3)

>>> []
>>> ['t', 25, 'cat', 3.1415]
>>> [1, 16, 49, 100, 169, 256, 484, 625, 784, 961, 1156, 1369, 1600, 1849, 2116, 2401, 2704, 3025, 3364, 3721, 4096, 4489, 4900, 5329, 5776, 6241, 7225, 7744, 8281,8836, 9409]


```

## Tuplas/ Tuples

a. Inmutalbe (no se pueden aniadir o cambiar)
b. Utiles para datos constantes, como un mapa con coordenadas de sitios arqueologicos, edificios, etc.
c. Mas rapidas que las listas
d. Tipo secuencial

```py

# Formas para construir tuplas

tuple1 = ()
tuple2 = (1274, 1275, 1276)
typle3 = 'mulan', 'pucca', 'percy'

print(tuple1)
print(tuple2)
print(tuple3)

>>> ()
>>> (1274, 1275, 1276)
>>> ('mulan', 'pucca', 'percy')

```

## Conjuntos/ Sets

a. Almacenan objetos no-duplciaods.
b. De acceso rapido.
c. Aceptan operaciones logicas.
d. Son desordenados.

Como una receta de cocina con ingredientes que no se duplican.

```py
# formas para construir conjuntos

set1 = {3, 5, 9, 3, 9}
set2 = set()
numbers = [1, 2, 3, 4, 5, 6, 1, 2]
set3 = set(numbers)

print(set1)
print(set2)
print(set3)

>>> {9, 3, 5}
>>> set()
>>> {1, 2, 3, 4, 5, 6}

```

## Diccionarios/ Diccionaries

a. Pares de llave/valor.
b. Arrays asociativos (hash maps).
c. Son ordenados.

Son rapidos para realizar consultas.

```py

cats1 = {
    'mulan': 2,
    'pucca': 1.2,
    'percy': 4,
}

cats2 = dict([('mulan', 2),('pucca', 1.2),('percy', 4)])
cats3 = dict(mulan=2, pucca=1.2, percy=4)

print(cats1)
print(cats2)
print(cats3)

>>> { 'mulan': 2, 'pucca': 1.2, 'percy': 4}
>>> { 'mulan': 2, 'pucca': 1.2, 'percy': 4}
>>> { 'mulan': 2, 'pucca': 1.2, 'percy': 4}

```

### ¿En qué casos usuarías cada estrcutura? ¿Qué tipo de información guardarías?

a. Listas: para una tienda en linea, para poder tener un control de los distintos tipos de producto, meteria listas que contengan strings para el nombre, codigo de barras, numeros para los precios y boleanos para saber si esta disponible o no el producto.

b. Tuplas: para la misma tienda en linea, para clasificar en secciones los diferentes productos, donde se definen de forma anticipada los tipos de productos que se venderan como estrategia de negocio y se supone que no cambiaran en el corto ni mediano plazo, en este caso serian puros strings y las categorias podrian ser, para una tienda en linea de productos deportivos: calzado, accesorios, conjuntos de ropa, pants, jerseys, shorts, etc.

c. Conjuntos o sets: para el carrito de compras en la tienda de ropa deportiva en el que en la mayor parte de los casos solo compraras un tipo de producto en especifico, quieres evitar duplicados al momento de hacer la transaccion de venta, y este tipo de estructuras puede ser un buen candado para evitar compras duplicadas, podrias ser por sku para ventas a individuos, en el caso de ventas a otras empresas o asociaciones deportivas, se podria vender con skus repetidos.

d. Diccionarios: para la tienda de articulos deportivos, lo usaria para guardar la informacion de cada usuario, como su nombre (strings), direccion (strings), edad(number), etc.

# Arrays

Primera estructura de datos lineales que conoceremos

## Que es una estructura de datos?

Representacion interna de una coleccion de informacion

## Conceptos claves

a. Elementos: valor que se almacena en cada una de las posiciones del array.
b. Indice: referencia a la posicion del elemento.

## Comportamiento de la Memoria

### Memory slot

Se puede visualizar como una rejilla donde de se almacenan datos, conforme se coloque informacion, estas casillas se iran ocupando.

### Como se guardan los datos

Se guardan de forma secuencial, pero cuando se elimina un dato, se crea un hueco, y los nuevos inputs de inforamcion que se quieran agregar, necesitaran acomodarse en espacios consecutivos disponibles de acuerdo al tamanio de su informacion

Los arrays guardan informacion de forma consecutiva y tiene restricciones.
No se puede guardar mas inforamcion que la permite un array.

Array tiene una capacidad que es el numero de elementos que puede almacenear.

Hay distintos tipos de array
a. Lineal
b. Dos dimensiones
c. Tres dimensiones

En python no se recomienda programar con estructuras de datos con mas de 2 dimensiones.

### Los arrays son listas?

Si, los arrays son un tipo de listas, pero las listas no son son arrays. Tienen ciertas restricciones:

No pueden:
a. agregar posiciones.
b. remover posiciones
c. modificar su tamanio
d. su capacidad se define al crearese.

Un caso de uso son los video juegos como los mapas de bits, para que la imagen no sea mas grande que la definida, o para los menus de opciones donde no habra nuevas opciones.

### Modulo array

Existe un modulo predefinido de arrays en python pero no es tan versatil porque:
a. Solo almacena numeros y caracteres
c. Badado en listas. No nos permite almacenar distintos tipos de datos.

# Crear un array

Creemos nustro propio array porque al definir sus metodos, entenderemos mejor como funciona. Un array puede tener metodos para:
a. Crearse
b. Longitud
c. Representacion string
d. Pertenencia
e. Indice
f. Reemplazo

# Arrays de dos dimensiones

Otros nombres:
a. Bi-dimensional array
b. Two-dimensional array
c. Grid
d. Grid
e. Rejilla
f. Malla
g. Tabla

## Estructura

Su estructura es una tabla con filas y columnas que en su interseccion tendra elementos, en un array cada elemento puede tener un valor diferente. Cuando en una lista anidamos otra mas, es un ejemplo de este tipo de estructuras.

## recapitulacio

a. creamos una clase grid a partir de una clase array
b. los valores por defecto eran none pero los cambiamos
c. hicimos referencia a cada uno de los datos en las filas y en las columnas con loops anidados.

## que pasa con los arrays de 3 dimensiones

Son arrays, dentro de arrays, dentro de arrays.

### Reto

a. Crear una clase 'Grid' - Incorporarle un metodo para cambiar sus valores, para que no sean non, como numeros aleatorios, secuenciales
b. Incorpora un metodo para poblar sus slots
c. Crea una clase 'Cube': array de 3 dimensiones

# Nodos y singly linked lists

## Linked structures

a. Consiste de nodos conectados unos a otros.
b. Los mas comunes son sencillos o dobles.
c. No se accede por indice, sino por recorrido.

Su estructura les da ciertas ventajas y desventajas

## Conceptos clave

a. Data: valor almacenado en los nodos.
b. Next: referencia al siguiente nodo.
c. Previous: referencia al nodo anterior.

Los valores no son secuenciales, no necesariamente son: 1, 2, 3, dependera del contenido del nodo.

d. Head: referencia al primer nodo en la lista.
e. Tail: referencia al ultimo nodo en la lista.

## como se guardan los linked list?

Los datos en los nodos estan repartidos en la memoria, no son contiguos, a difrencia de los arrays. Para hacer referencia a otro dato, usamos los nodos que se van a concectar a otro dato, que esta en otro espacio en la memoria.

Con esto podemos saltar entre espacios de memoria, mas rapido, que usando una lista

## implementacion o como podemos implementarlas

a. Implementar otras estructuras
b. Optimizacion

Los nodos nos sirven para crear estructuras mas complejas, como los stacks o queues, y podemos optimizar nuestro codigo usando linked list cuando las opciones no son muchas.

## Singly linked structures

[head] -> [D1| ] -> [dato|referencia] -> [D3| ] -> [D4|none]

Tambien pueden ser double linked lists o structures, tienen un comportamiento diferente donde los nodos tienen referencia al nodo siguiente y al anterior

## casos de uso

a. Hacer/ rehacer operaciones en un editor de texto
b. Historial de un navegador

Hay que tener creatividad y criterio para crearlas porque si una lista crece demasiado, sera mas dificil de gestionar.

```
https://platzi.com/home/clases/2299-estructuras-datos-python/37651-nodos-y-singly-linked-list/
```

# Crear nodos

Te permiten crear estructuras de datos mas complejas, y cada nodo va almacenar un dato, y cada nodo va a puntar a otro nodo.
Esto va a aser muy util si tenemos informacion dispersa en memoria y no podemos almacenarla toda en el mismo espacio.

## Single linked list con nodos

a. Crearemos una clase Node.
b. Referimos valores.
c. Unimos nodos iterando.

# Crear singly linked list

