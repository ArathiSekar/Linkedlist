#Given a singly linked list, return another linked list that is the reverse of the first.

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    
class createLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self,value):
        if(self.head is None):
            self.head = Node(value)
            self.tail = self.head
        
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
    
    #def prepend(self,value):
    #    if(self.head is None):
    #        self.head = Node(value)
        
    #    else:
    #        new_node = Node(value)
    #        new_node.next = self.head
    #        self.head = new_node
    
def reverseLinkedList(ll):
    if (ll.head is None):
        return None        
    else:
        new_linkedlist = createLinkedList()
        prev_node = None    
        current_node = ll.head
        while(current_node):
            #new_linkedlist.prepend(current_node.value)
            #current_node = current_node.next
            new_node = Node(current_node.value)
            new_node.next = prev_node
            prev_node = new_node
            current_node = current_node.next
            
        new_linkedlist.head = prev_node
               
    #Print
    current_node = new_linkedlist.head
    while(current_node):
        print(current_node.value)
        current_node = current_node.next

    
ll = createLinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)

reverseLinkedList(ll)

