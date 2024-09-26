'''
Ejemplo 1: Implementacion basica de una lista enlazada simple
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
            
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print('None')
        
if __name__ == '__main__':
    from ejemplo1 import Node, LinkedList
    
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.display()
    
    '''
    1 -> 2 -> 3 -> None
    '''
    
    la = LinkedList()
    la.append(4)
    la.append(3)
    la.append(2)
    la.append(1)
    la.append(ll)
    la.display()
    
    '''
    4 -> 3 -> 2 -> 1 -> <ejemplo1.LinkedList object at 0x7f8ae74dfc10> -> None
    
    se puede guardar una linked list, dentro de una linked list
    '''