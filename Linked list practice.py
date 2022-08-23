#Implement a linked list class. You have to define a few functions that perform the desirbale action. Your LinkedList class should be able to:

#Append data to the tail of the list 
#prepend data to the head
#Search the linked list for a value and return the node
#Remove a node
#Pop, which means to return the first node's value and delete the node from the list
#Insert data at some position in the list
#Return the size (length) of the linked list

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    
class createLinkedlist:
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
        

    def prepend(self,value):
        if (self.head is None):
            self.head = Node(value)
            self.tail = self.head
        
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
            
    def search(self,value):
        if(self.head is None):
            return None
        else:
            current_node = self.head
            while(current_node):
                if(value == current_node.value):
                    return current_node.value
                else:
                    current_node = current_node.next
    
    
    def remove(self,value):
        if(self.head is None):
            return None
        elif (self.head.value == value):
            self.head = self.head.next
        else:
            current_node = self.head
            while(current_node.next):
                if(value == current_node.next.value):
                    current_node.next = current_node.next.next
                else:
                    current_node = current_node.next
                    
        
    def pop(self):
        if (self.head is None):
            return None
        else:
            pop_value = self.head.value
            self.head = self.head.next
            return pop_value
    
    
    def insert(self,value,pos):
        if (self.head is None):
            return None
        elif (pos == 0):
            current_node = Node(value)
            current_node.next = self.head
            self.head = current_node
        
        else:
            count = 1
            current_node = self.head
            while(current_node.next and count<=pos):
                if(pos == count):
                    new_node = Node(value)
                    #print(new_node.value)
                    new_node.next = current_node.next
                    current_node.next = new_node
                    return self.head
                count +=1
                current_node = current_node.next
                
        self.append(value)
    
    
    def size(self):
        if(self.head is None):
            return 0
        else:
            current_node = self.head
            length_linkedlist = 0
            while(current_node):
                length_linkedlist +=1
                current_node = current_node.next
        
        return length_linkedlist
    
ll = createLinkedlist()
ll.append(1)
ll.append(2)
ll.append(4)
ll.append(5)
ll.prepend(3)
ll.remove(2)
searched_value = ll.search(2)
print ("Searched node value is {}".format(searched_value))

pop_value = ll.pop()
print ("Popped value is {}".format(pop_value))

ll.insert(6,6)

length_linkedlist = ll.size()
print("Length of LinkedList is {}".format(length_linkedlist))

current_node = ll.head
while(current_node):
    print(current_node.value)
    current_node = current_node.next
