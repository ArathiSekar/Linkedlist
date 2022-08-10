#Implement a doubly linked list that can append to the tail in constant time. Make sure to include forward and backward connections when adding a new node to the list.
class DoubleNode():
    def __init__(self,value):
        self.value = value
        self.next = None
        self.previous = None
    
class createDoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        
    def append(self,value):
        if(self.head is None):
            self.head = DoubleNode(value)
            self.tail = self.head
        
        else:
            self.tail.next = DoubleNode(value)
            self.tail.next.previous = self.tail
            self.tail = self.tail.next

ll = createDoublyLinkedList()
ll.append(1)
ll.append(2)
ll.append(3)

current_node = ll.head
print("Going forward through the list")
while(current_node):
    print(current_node.value)
    current_node = current_node.next

print("Going backward through the list")
current_node = ll.tail
while(current_node):
    print(current_node.value)
    current_node = current_node.previous
