class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class createLinkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
    
    #def append(self,value):
     #   if (self.head is None):
     #       self.head = Node(value)
             
      #  else:
      #      current_node = self.head
       #     while (current_node.next):
      #          current_node = current_node.next
     #       current_node.next = Node(value)    
                
              
    def append(self,value):
        if(self.head is None):
            self.head = Node(value)
            self.tail = self.head
        
        else:
            self.tail.next = Node(value) 
            self.tail = self.tail.next
    
   
    def to_list(self):
    # Write function to turn Linked List into Python List
        python_list = []
        current_node= self.head
        while(current_node):
            python_list.append(current_node.value)
            current_node = current_node.next
        
        print(python_list)    

ll = createLinkedlist()

#ll.append(1)
#ll.append(2)
#ll.append(3)
input_list = [1,2,3,4,5]
for i in input_list:
    ll.append(i)

ll.to_list()
current_node = ll.head

while(current_node is not None):
    print(current_node.value)
    current_node = current_node.next
