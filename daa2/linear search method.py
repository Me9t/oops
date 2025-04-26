import time

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# Example usage for Linear Search
arr = [2, 4, 6, 8, 10, 14, 16, 17, 19, 20, 21, 25, 28, 29]

start = time.time()
result = linear_search(arr, 28)
end = time.time()

print(f"Linear Search took {(end - start) * 1000:.6f} ms. Found at index: {result}")
