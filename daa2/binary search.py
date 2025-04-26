import time

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

# Example usage for Binary Search
arr = [2, 4, 6, 8, 10, 14, 16, 17, 19, 20, 21, 25, 28, 29]

start = time.time()
result = binary_search(arr, 28)
end = time.time()

print(f"Binary Search took {(end - start) * 1000:.6f} ms. Found at index: {result}")
