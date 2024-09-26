'''
Eliminar un Nodo por Valor
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            
    def delete(self, key):
        current = self.head
        if current and current.data == key:
            self.head = current.next
            current = None
            return
        
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
            
        if current is None:
            return
        
        prev.next = current.next
        current = None
        
    def display(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print('None')
            
if __name__ == '__main__':
    from ejemplo3 import LinkedList
    
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.display()
    
    # 1 -> 2 -> 3 -> 4 -> None
    
    ll.delete(4)
    ll.display()
    
    # 1 -> 2 -> 3 -> None
    
    ll.delete(2)
    ll.display()
    
    # 1 -> 3 -> None
    
    ll.delete(1)
    ll.display()
    
    # 3 -> None