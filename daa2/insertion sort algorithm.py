def insertion_sort(arr):
    n = len(arr)

    # Step 1: If the element is the first element, assume it is already sorted
    if n <= 1:
        return arr

    # Step 2: Iterate through the array starting from the second element
    for i in range(1, n):
        # Step 2: Pick the next element and store it separately in a key
        key = arr[i]
        j = i - 1

        # Step 3: Compare the key with all elements in the sorted array
        # Step 4: If the element in the sorted array is smaller, move it
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # Step 5: Insert the value
        arr[j + 1] = key

    # Step 6: Return the sorted array
    return arr

# Example usage:
arr = [12, 11, 13, 5, 6]
sorted_arr = insertion_sort(arr)
print("Sorted array (Insertion Sort):", sorted_arr)
