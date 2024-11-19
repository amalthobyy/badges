class Node:
    def __init__(self,data):
        self.data= data
        self.next= None
class Linkedlist:
    def __init__(self):
        self.head= None
        self.tail=None
    def addNode(self,data):
        new_node= Node(data)

        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
    def deleteNode(self,data):
        temp=self.head 
        prev=None

        if temp.data == data:
            self.head=temp.next
            temp.next=None
        while temp is not None and temp.data!=data:
            prev=temp
            temp=temp.next
        if temp.data == self.tail:
            self.tail =prev
            prev.next=None
            return
        prev.next=temp.next

    def printrev(self,node):
        if node is None:
            return
        self.printrev(node.next)
        print(node.data,end="<--")
    def print(self):
        n=self.head
        if n is None:
            print("linkedlist is empty")
        else:
            while n is not None:
                print(n.data,end="-->")
                n=n.next
    def merge(self,other_list):
        if not self.head:
            self.head=other_list.head
        else:
            n=self.head
            while n.next:
                n=n.next
            n.next=other_list.head
arr1=[2,34,5,68,56,1]
ll2=Linkedlist()
for j in arr1:
    ll2.addNode(j)
arr=[1,2,3,4,5,6,7,8,9]
ll1=Linkedlist()
for i in arr:
    ll1.addNode(i)
# ll1.printrev(ll1.head)    

ll1.merge(ll2) 
ll1.print()                                        

       