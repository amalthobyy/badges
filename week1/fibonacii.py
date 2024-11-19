def fibonaci(n):
    if n<=1:
         return n
    else:
         return fibonaci(n-1)+fibonaci(n-2)
    
num=10
for i in range(num):
     print (fibonaci(i),end="")    

   
