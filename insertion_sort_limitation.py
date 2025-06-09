import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# small array
# arr = [40, 10, 3, 20, 50, 35,30, 90]

# large reverse sorted array (worst case)
arr = list(range(10000, 0, -1))

start_time = time.time()
insertion_sort(arr)
end_time = time.time()

print("\n\nSorted array:", arr)
print("\n\nTime taken:", end_time - start_time, "seconds\n\n\n")
