'''
Ejemplo 5: Invertir la Lista Enlazada
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

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        
    def display(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print('None')

if __name__ == '__main__':
    from ejemplo5 import LinkedList
    
    ll = LinkedList()
    ll.append(0)
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.display()
    
    ll.reverse()
    ll.display()
    
    la = LinkedList()
    la.append('a')
    la.append('b')
    la.append('c')
    la.append('d')
    la.display()

    la.reverse()
    la.display()