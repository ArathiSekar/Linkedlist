#Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.
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

class Solution:
    def getIntersectionNode(self, headA, headB):
        current_nodeA = headA
        current_nodeB = headB
                
        while(current_nodeA != current_nodeB):
            if (current_nodeA is None):
                current_nodeA = headB    
            current_nodeA = current_nodeA.next
            if (current_nodeB is None):
                current_nodeB = headA
            current_nodeB = current_nodeB.next
            
        print (current_nodeA.value)

ll1 = createLinkedList()
for i in [4,1]:
    ll1.append(i)

node1 = ll1.head
while(node1.next):
    #print(node1.value)
    node1 = node1.next

ll3 = createLinkedList()
for i in [8,4,5]:
    ll3.append(i)

node1.next = ll3.head

ll2 = createLinkedList()
for i in [5,6,1]:
    ll2.append(i)

node2 = ll2.head
while(node2.next):
    #print(node2.value)
    node2 = node2.next

node2.next = ll3.head
    
headA = ll1.head
headB = ll2.head

s = Solution()
s.getIntersectionNode(headA,headB)
