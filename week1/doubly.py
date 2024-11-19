class Node:
    def __init__(self,data):
        self.data= data
        self.next= None
        self.prev= None

class doubly:
    def __init__(self):
        self.head = None
        self.tail = None
    def add_node(self,data):
        new_node= Node(data)

        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next = new_node
            new_node.prev=self.tail
            self.tail = new_node
    def delete_node(self,data):
        temp = self.head
        if temp is not None and temp.data == data:
            if temp.next is not None:
                self.head = temp.next
                self.head.prev=None
            else:
                self.head=None
                self.tail= None
            return
        while temp is not None and temp.data!= data:
            temp=temp.next
        if temp is None:
            return
        if temp ==self.tail:
            self.tail=self.tail.prev
            self.tail.next=None
        else:                                                     
            temp.prev.next=temp.next
            if temp.next is not None:
                temp.next.prev=temp.prev
    def print_Dl(self):
        n=self.head
        while n is not None:
            print(n.data,end="<-->")
            n=n.next


arr=[1,2,3,4,45,6,72,7,45,7]  
dll= doubly()
for i in arr:
    dll.add_node(i)

dll.print_Dl()                         


