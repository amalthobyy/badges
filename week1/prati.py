class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head= None
        self.tail= None
    def add_node(self,data):
        new_node=Node(data)

        if self.head is None:
            self.head =new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail=new_node
    def print_ll(self):
        n=self.head
        if n is None:
            print("empty")
        else:
            while n is not None:
                print (n.data,end="-->")
                n=n.next

arr=[1,2,3,4,5,6,7,8]
ll1=linkedlist()
for i in arr:
    ll1.add_node(i)
ll1.print_ll()                 