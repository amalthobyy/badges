def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if arr[j] < arr[min]:
                min=j
        arr[i],arr[min]=arr[min],arr[i]
    return arr
arr=[1,7,23,2,4,5,7,33,9]
print (selection_sort(arr))            