class Array:
    def __init__(self, capacity, fill_value=None):
        self.items = list()
        for i in range(capacity):
            self.items.append(fill_value)
            
    def __len__(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
    
    def __iter__(self):
        return iter(self.items)
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __setitem__(self, index, new_item):
        self.items[index] = new_item
        
        
menu = Array(5)

# tiene sus propios pero tambien puede utilizar los de 

# ITERANDO CON METODOS PROPIOS DE PYTHON

print(len(menu))

print(menu)

for i in range(len(menu)):
    menu[i] = i + 1
    
print(menu[0])

print(menu[1])

print(menu[2])

print(menu)

# recorrer para explorar

for option in menu:
    print(menu[option - 1])
    
# ITERANDO CON METODOS CREADOS

class Array:
    def __init__(self, capacity, fill_value=None):
        self.items = list()
        for i in range(capacity):
            self.items.append(fill_value)
            
    def __len__(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
    
    def __iter__(self):
        return iter(self.items)
    
    def __getitem__(self, index):
        return self.items[index]
    
    def __setitem__(self, index, new_item):
        self.items[index] = new_item

menu = Array(5)

for i in range(len(menu)):
    menu[i] = i + 1

print(menu.__len__())

print(menu.__str__())

print(menu.__iter__()) # muestra la referencia en memoria

print(menu.__getitem__(2))

print(menu.__setitem__(2, 100))

print(menu)
