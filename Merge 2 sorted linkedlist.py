#Merge 2 sorted linked lists in ascending order

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None
    
    def append(self,value):
        if(self.head is None):
            self.head = Node(value)
            
        else:
            current_node = self.head
            
            while(current_node.next):
                current_node = current_node.next
                
            current_node.next = Node(value)
           
    def to_list(self):
        out = []
        current_node = self.head
        
        while(current_node):
            #print(current_node.value)
            out.append(current_node.value)
            current_node = current_node.next    
        
        print(out)
    
    def printLinkedlist(self):
        current_node = self.head
        while(current_node):
            print(current_node.value)
            current_node = current_node.next
        


def merge(list1,list2):
    list1_elt = list1.head
    list2_elt = list2.head
    merged_node = Node(0)
    temp_node = merged_node
    if (list1_elt is None):
        return list2.head
    elif (list2_elt is None):
        return list1.head
    else:
        while(list1_elt or list2_elt):
            if (list1_elt is None):
                merged_node.next = list2_elt
                list2_elt = list2_elt.next
            elif (list2_elt is None):
                merged_node.next = list1_elt
                list1_elt = list1_elt.next
            elif(list1_elt.value <= list2_elt.value):
                merged_node.next = list1_elt
                list1_elt = list1_elt.next
            else:
                merged_node.next = list2_elt
                list2_elt = list2_elt.next
           
            merged_node = merged_node.next
    return(temp_node.next)
        
ll1 = Linkedlist()
ll1.append(1)
ll1.append(4)
ll1.append(6)
#ll1.to_list()
#ll1.printLinkedlist()

ll2 = Linkedlist()
ll2.append(2)
ll2.append(3)
ll2.append(5)
#ll2.to_list()        
                
temp_node = merge(ll1,ll2)

node = temp_node
while node is not None:
    print(node.value)
    node = node.next
