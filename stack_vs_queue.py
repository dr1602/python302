# Ejemplo utilizando un stack sencillo
from stack import Stack
hot_cakes = Stack()

hot_cakes.push('banana pancake')
hot_cakes.push('chocolate chip')
hot_cakes.push('blueberry pancake')

print(hot_cakes)

print(hot_cakes.pop())

print(hot_cakes)


# Ejemplo utilizando un queue sencillo

from queue import Queue
hot_cakes = Queue()

hot_cakes.put('banana pancake')
hot_cakes.put('chocolate chip')
hot_cakes.put('blueberry pancake')

print(hot_cakes)
print(list(hot_cakes.queue))

print(hot_cakes.get())

print(hot_cakes)
print(list(hot_cakes.queue))