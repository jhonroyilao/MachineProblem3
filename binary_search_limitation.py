def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # if target is found
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1  # Target not found

#SORTED array
# arr = [3, 10, 20, 30, 35, 40, 50, 90]

# UNSORTED array (to demonstrate limitation)
arr = [40, 10, 3, 20, 50, 35,30, 90]
target = 30

# attempting binary search on unsorted data
result = binary_search(arr, target)
print("\n\nResult index (on unsorted array):", result)
print("\n\n")
