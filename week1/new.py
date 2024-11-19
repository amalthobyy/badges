def binary(arr,target):
    arr.sort()
    low=0
    high= len(arr)-1

    while low<=high:
        mid=(low + high)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid -1
        else:
            low = mid +1
    return -1
arr= [1, 3, 4, 5, 6, 9, 11, 15, 18, 21, 25]
target=15
print(binary(arr,target))            