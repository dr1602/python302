from node import Node

head = None
index = 3

if head is None or index <= 0:
    print("Invalid index or empty list")
elif index <= 0 or head.next is None:
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
    print(removed_item)

# Invalid index or empty list