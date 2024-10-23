class Node:
    def __init__(self,data):
        self.data =data
        self.next=None
class linkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def add_node(self,data):
        new_node=Node(data)

        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
    def printLL(self):
        if self.head is None:
            print("ll is emptty")
        else:
            n=self.head
            while n is not None:
                print(n.data,end="-->")
                n=n.next


arr=[1,2,3,4,5,6,7,8]
ll1=linkedList()
for i in arr:
    ll1.add_node(i)
ll1.printLL()    