# class BST:
#     def __init__(self,key):
#         self.key=key
#         self.lchild=None
#         self.rchild=None
#     def insert(self,data):
#         if self.key is None:
#             self.key=data
#             return
#         if self.key==data:
#             return
#         if self.key>data:
#             if self.lchild:
#                 self.lchild.insert(data)
#             else:
#                 self.lchild=BST(data)
#         else:
#             if self.rchild:
#                 self.rchild.insert(data)
#             else:
#                 self.rchild=BST(data)

#     def inorder(self):
#         if self.lchild:
#             self.lchild.inorder()
#         print(self.key,end=" ")
#         if self.rchild:
#             self.rchild.inorder()

    
        
    

# root=BST(10)
# list1=[1,2,3,5,7,9]
# for i in list1:
#     root.insert(i)
# print (root.inorder()) 
# value=4
# print(root.trueorfalse(5)) 



def heapify(arr,n,i):
    largest = i
    left = 2*i+1
    right=2*i+2

    if left < n and arr[left]>arr[largest]:
        largest=left
    if right< n and arr[right]>arr[largest]:
        largest=right
    if i!=largest:
        arr[i],arr[largest]=arr[largest],arr[i]
        heapify(arr,n,largest)
def inorder(arr):
    n=len(arr)
    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i)
    for j in range(n-1,0,1):
        arr[i],arr[0]=arr[0],arr[i]
        heapify(arr,i,0)

arr=[1,3,5,6,2,7]
inorder(arr)
print(arr)


               

     
    