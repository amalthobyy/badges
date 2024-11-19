class Queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self, item):
        self.queue.append(item)
        print(item, 'enqueued to Queue')
    def dequeue(self):
        if len(self.queue)==0:
            print('Queue is empty!')
        else:
            item=self.queue.pop(0)
            print(item, 'is dequeued')
            return item
    def peek(self):
        if len(self.queue)==0:
            print('Queue is empty!')
        else:
            element=self.queue[0]
            print(element, 'is at the front')
    def display(self):
        if len(self.queue)==0:
            print('Queue is empty!')
        else:
            print('Queue from front to end:')
            for item in self.queue:
                print(item)
q=Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.peek()
q.display()