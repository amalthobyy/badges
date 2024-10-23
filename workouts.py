class Node:
    def __init__(self,data):
        self.data= data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None


    def add_node(self,data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail =new_node 

    def print_node(self):
        if self.head is None:
            print("ll is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n=n.next


arr =[ 1,2,3,3,4,5,5,]
a= Linkedlist()
for i in arr:
    a.add_node(i)

a.print_node()    
  
