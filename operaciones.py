[]

['Isabel']

['Isabel', 'Mulan']

['Isabel', 'Mulan', 255]

['Isabel', 'Mulan', 255, ['Pucca', 'Percy']]

fruits = []

fruits.append('Kiwi')
fruits.append('Manzana')
fruits.append('Uva')
fruits.append('Arandano')

print(fruits)

fruits.sort()
print(fruits)

fruits.pop()
print(fruits)

fruits.insert(0, 'Mandarina')
print(fruits)

fruits.insert(1, 'Berry')
print(fruits)

fruits.pop(1)
fruits.sort()
print(fruits)

fruits.remove('Uva')
print(fruits)

fruits.remove('Dragon Fruit')
print(fruits)

# Ejemplo con funciones.

## Funcion que sume numeros pero que los muestre en forma de piramide

def pyramid_sum(lower, upper, margin=0):
    blanks = " " * margin
    print(blanks, lower)
    if lower > upper:
        print(blanks, 0)
        return 0
    else:
        result = lower + pyramid_sum(lower + 1, upper, margin + 4)
        print(blanks, result)
        return result
    
pyramid_sum(1, 4)

## hace las operaciones de forma recursiva, usaremos funciones asi para construir estrucutras de datos
## estas funciones seran metodos de calses especificas de las estructuras
## poner atenciona detalle para entender