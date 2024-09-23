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
