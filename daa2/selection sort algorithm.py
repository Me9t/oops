def selection_sort(arr):
    n = len(arr)

    
    for i in range(n):
    
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

my_array = [64, 25, 12, 22, 11]
selection_sort(my_array)
print("Sorted array (Selection Sort):", my_array)
