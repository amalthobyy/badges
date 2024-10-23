class Node:
    def __init__(self,data):
        self.data= data
        self.next= None
class linked_list:
    def __init__(self):
        self.head=None
        self.tail=None

    def add(self,data):
        new_node=Node(data)

        if self.head is None:
            self.head = new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node

    def delete_node(self,data):
        temp=self.head
        prev=None


        if temp.data==data:
            self.head=temp.next
            temp.next=None

        while temp is not None and temp.data!=data:
            prev=temp
            temp=temp.next

        if temp.data==self.tail:
            self.tail=prev
            prev.next = None
            return
        prev.next=temp.next




    def print_ll(self):
        if self.head is None:
            print("empty linked list")

        else:
            n= self.head
            while n is not None:
                print(n.data)
                n=n.next



arr=[1,3,4,6,7,9,4]
ll1=linked_list()
for i in arr:
    ll1.add(i)
ll1.print_ll()    


    

