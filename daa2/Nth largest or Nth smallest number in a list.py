def nth_largest_sort(arr, n):
    sorted_arr = sorted(arr, reverse=True)  # Sorting in descending order
    return sorted_arr[n - 1]

def nth_smallest_sort(arr, n):
    sorted_arr = sorted(arr)  # Sorting in ascending order
    return sorted_arr[n - 1]

# Example usage:
arr = [12, 3, 45, 7, 22, 18, 90, 1, 67, 34]
n = 3  # Find the 3rd largest or smallest

# Finding the Nth largest number
result_largest = nth_largest_sort(arr, n)
print(f"The {n}rd largest number is: {result_largest}")

# Finding the Nth smallest number
result_smallest = nth_smallest_sort(arr, n)
print(f"The {n}rd smallest number is: {result_smallest}")
