class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
    def addNode(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head= new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail=new_node

    def printLL(self):
        n=self.head
        if n is None:
            print("empty linked list")
        else:
            while n is not None:
                print (n.data,end="-->")
                n=n.next


    def delet_node(self,data):
        temp = self.head
        prev= None
        




arr=[1,2,3,4,5,23,6,87,8]
ll1=Linkedlist()
for i in arr:
    ll1.addNode(i)

ll1.printLL()                                
