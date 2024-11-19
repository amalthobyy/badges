def linear_search(arr, target):
    for i in arr:
        if i  == target:
            return i
    return -1

arr = [4,7,53,2,34,75,12,1,5,3]
target=53
print(linear_search(arr, target))

