'''
Insertar al Inicio de la Lista
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def display(self):
        current = self.head
        
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print('None')
        
if __name__ == '__main__':
    from ejemplo2 import Node, LinkedList
    
    ll = LinkedList()
    ll.prepend(3)
    ll.prepend(2)
    ll.prepend(1)
    ll.prepend(0)
    ll.display()
    
    la = LinkedList()
    la.prepend(0)
    la.prepend(1)
    la.prepend(2)
    la.prepend(3)
    la.prepend(ll)
    la.display()