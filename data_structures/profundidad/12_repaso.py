from node import Node

# Creacion de los nodos enlazados (linked list)

head = None

for count in range(1,6):
    head = Node(count, head)

# * Recorrer e imprimir valores de la lista

probe = head
print('Recorrido de la lista:')

while probe != None:
    print(probe.data)
    probe = probe.next

'''
Recorrido de la lista:
5
4
3
2
1
'''

# * Remplazo de un elemento
probe = head
target_item = 3
new_item = 'Z'

while probe != None and target_item != probe.data:
# mientras probe is diferente a None y el valor objetivo es diferente al valor en data
    probe = probe.next
    # avanzas al siguiente nodo, para si alguna de las condiciones se cumple

if probe != None:
# si el nodo es diferente a None...
    probe.data = new_item
    # el valor del nodo actual se convierte en el valor asignado en new item
    print(f'{new_item} replace the old value in the node number {target_item}')
else:
# si el valor es igual a none, el valor objetivo no esta en la lista
    print(f'The target item {target_item} is not in the linked list')

# Z replace the old value in the node number 3
# lo que ahora quiero entender, es para que sirve probe si queremos sustituir??? 
# incluso para que sirve si recorreremos los nodos.

while probe != None:
    print(probe.data)
    probe = probe.next

'''
Z
2
1
'''

# se perdieron las valores anteriores a Z

# * Insertar un nuevo elemento/nodo al inicio (head)
head = Node('F', head)

while head != None:
    print(head.data)
    head = head.next

# F
# 5
# 4
# Z
# 2
# 1

# * Insertar un nuevo elemento /nodo al final(tail)
new_node = Node('K')

if head is None:
    head = new_node
else: 
    probe = head
    while probe.next != None:
        probe = probe.next
    probe.next = new_node

while head != None:
    print(head.data)
    head = head.next

'''
F
5
4
Z
2
1
K
'''

# * Eliminar un elemento/nodo a inicio(tail)
'''
removed_item = head.data
head = head.next
print('Removed_item: ', end='')
print(removed_item)
'''

# * Eliminar un elemento/nodo al final(tail)
'''
removed_item = head.data
if head.next is None:
    head = None
else:
    probe = head
    while probe.next.next != None:
        probe = probe.next
    removed_item = probe.next.data
    probe.next = None

print('Removed_item: ',end='')
print(removed_item)
'''

# * Agregar un nuevo elemento/nod por 'indice' inverso (Cuenta de Head - Tail)
# new_item = input('Enter new item: ')
# Index = int(input('Enter the position to insert the new item: '))
new_item = '10'
index = 3

if head is None or index <= 0:
    head = Node(new_item, head)
else:
    probe = head
    while index > 1 and probe.next != None:
        probe = probe.next
        index -= 1
    probe.next = Node(new_item, probe.next)

# * Agregar un nuevo elemento/nod por 'indice' inverso (cuenta de head - tail)

'''
Recorrido de la lista:
5
4
Z
10
2
1
'''

# * Eliminar un nuevo elemento/nodo por 'indice' inverso(cuneta de Head - Tail)

index = 3

if head is None or index <= 0:
    removed_item = head.data
    head = head.next
    print(removed_item)
else:
    probe = head
    while index > 1 and probe.next.next != None:
        probe = probe.next
        index -= 1
    removed_item = probe.next.data
    probe.next = probe.next.next

    print("Removed_item: ",end="")
    print(removed_item)

