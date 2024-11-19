class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 

class linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, data):
        new_node = Node(data)   

        if self.head is None:
            self.head = new_node  
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def node_delete(self, data):
        temp = self.head
        prev_node = None

        if temp.data == data:
            self.head = temp.next
            temp.next = None

        while temp is not None and temp.data != data:
            prev_node = temp
            temp = temp.next
        
        if temp.data == self.tail:
            self.tail = prev_node
            prev_node.next = None
            return

        prev_node.next = temp.next


    def print_LL(self):
        if self.head is None:
            print("ll is empty") 
        else:
            n = self.head
            while n is not None:
                print(n.data, end=" --> ")
                n= n.next

arr = [3,5,7,74,2,6,67,32,56]
ll1=linkedlist()
for i in arr:
    ll1.add_node(i)


ll1.node_delete(56)
ll1.print_LL()


