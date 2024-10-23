class Node:
    def __init__(self,data):
        self.data=data
        self.next= None
class Linkedlist:
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


    def delete_node(self,data):

        temp=self.head
        prev=None

        if temp.data ==data:
            self.head = temp.next
            temp.next=None
        while temp is not None and temp.data!=data:
            prev=temp
            temp=temp.next
        if temp.data==self.tail:
            self.tail=prev
            prev.next=None
            return

        prev.next =temp.next
    
    def add_node_after(self, target, data):
        temp = self.head

        while temp and temp.data != target:
            temp = temp.next

        new_node = Node(data)

        temp.next = new_node
        new_node.next = 




    def printll(self):
        if self.head is None:
            print("empty ll")
        else:
            n=self.head
            while n is not None:
                print(n.data,end="-->")
                n=n.next 

arr=[1,3,4,5,7,8,9,9,2,3]

ll1=Linkedlist()
for i in arr:
    ll1.add_node(i)


ll1.delete_node(5)  
ll1.add_node_after(4)
ll1.add_node(10)
ll1.printll()  





