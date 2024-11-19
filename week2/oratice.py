# def merge_sort(arr):
#     if len(arr)>1:
#         mid=len(arr)//2
#         left_list=arr[:mid]
#         right_list=arr[mid:]
#         merge_sort(left_list)
#         merge_sort(right_list)
#         i=0
#         j=0
#         k=0
#         while i<len(left_list)and j<len(right_list):
#             if left_list[i]<right_list[j]:
#                 arr[k]=left_list[i]
#                 i+=1
#                 k+=1
#             else:
#                 arr[k]=right_list[j]
#                 j+=1
#                 k+=1
#         while i<len(left_list):
#             arr[k]=left_list[i]
#             i+=1
#             k+=1
#         while j<len(right_list):
#             arr[k]=right_list[j]
#             j+=1
#             k+=1


# arr=[1,4,2,6,8,3,8]
# merge_sort(arr)
# print (arr)                      

# def insertion_sort(arr):
#     for i in range(1,len(arr)):
#         key=arr[i]
#         j=i-1
#         while j>=0 and key<arr[j]:
#             arr[j+1]=arr[j]
#             j-=1
#             arr[j+1]=key
#     return arr
# arr=[8,4,7,1,8,3,0,2,7] 
# print(insertion_sort(arr))       
# class Stack:
#     def __init__(self):
#         self.stack=[]
#     def push(self,item):
#         self.stack.append(item)
#         print(item,"is added to the stack")
#     def peek(self):
#         if not self.is_empty():
#             element=self.stack[-1]
#             print(element,"is on the top of the stack")
#     def pop(self):
#         if len(self.stack)==0:
#             print("stack is empty")
#         else:
#             item=self.stack.pop()
#             print(item,'is removed from the stack')
#             return item
#     def display(self):
#         for item in reversed(self.stack):
#             print(item)
# s=Stack()
# s.push(10) 
# s.push(12)   
# s.push(17)   
# s.push(18) 
# s.pop()

# s.display()                 





class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,item):
        self.stack.append(item)
        print(item,"is add to the stack")
    def pop(self):
        if len(self.stack)==0:
            print("stack is empty")
        else:
            item=self.stack.pop()
            print(item," removed from the stack")
            return item 
    def display(self):
        for i in self.stack:
            print(i)
s=Stack()
s.push(10)
s.push(20)
s.push(12)
s.push(14)
s.pop()
s.display()
                                         
