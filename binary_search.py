def binary_search(arr, target):
    
    arr.sort()
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1  

arr = [23, 6, 4, 7, 4332, 7, 3, 47, 45, 3]
target = 7
result = binary_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result} in the sorted array.")
else:
    print(f"Element {target} not found.")
