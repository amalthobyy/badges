class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,item):
        self.stack.append(item)
        print(item,("is added to the stack"))
    def display(self):
       
        for i in reversed(self.stack):
            print(i)  

s=Stack()
s.push("amal")
s.display()            
