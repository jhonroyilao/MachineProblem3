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

# large reverse sorted array
arr = list(range(10000, 0, -1))

start_time = time.time()
insertion_sort(arr)
end_time = time.time()

print("\n\nTime taken to sort reverse sorted array of size 10,000:", end_time - start_time, "seconds\n\n\n")
