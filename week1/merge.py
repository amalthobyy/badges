class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedL:
    def __init__(self):
        self.head=None
        self.tail=None
    def add_node(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next =new_node
            self.tail= new_node

    def merge(self, other_list):
        if not self.head:
            self.head=other_list.head
        else:
            n=self.head
            while n.next:
                n= n.next
            n.next=other_list.head

    def print(self):
        n= self.head
        if n is None:
            print("LL empty")
        else:
            while n is not None:
                print (n.data,end="-->")
                n=n.next


    def rev(self,node):
        if node is None:
            return
        self.rev(node.next)
        print(node.data,end="<--")            

    




arr=[1,3,4,5,6,7,8,9,1,3]
arre=[9,8,76,5,42]

ll1=LinkedL()
for i in arr:
    ll1.add_node(i)
ll2=LinkedL()
for j in arre:
    ll2.add_node(j)

ll1.merge(ll2)

ll1.rev(ll1.head)
