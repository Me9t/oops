import time
import heapq

# Function to find the Nth maximum element using sorting
def nth_max_sort(lst, n):
    sorted_list = sorted(lst, reverse=True)
    return sorted_list[n - 1]

# Function to find the Nth maximum element using heapq.nlargest
def nth_max_heap(lst, n):
    return heapq.nlargest(n, lst)[-1]

# Function to find the Nth maximum element using max function iteratively
def nth_max_max(lst, n):
    temp_lst = lst.copy()  # Avoid modifying the original list
    for _ in range(n - 1):
        temp_lst.remove(max(temp_lst))
    return max(temp_lst)

# Function to find the Nth minimum element using sorting
def nth_min_sort(lst, n):
    sorted_list = sorted(lst)
    return sorted_list[n - 1]

# Function to find the Nth minimum element using heapq.nsmallest
def nth_min_heap(lst, n):
    return heapq.nsmallest(n, lst)[-1]

# Function to find the Nth minimum element using min function iteratively
def nth_min_min(lst, n):
    temp_lst = lst.copy()  # Avoid modifying the original list
    for _ in range(n - 1):
        temp_lst.remove(min(temp_lst))
    return min(temp_lst)

# Function to compare efficiency of algorithms
def compare_algorithms(lst, n):
    algorithms = {
        "Sorting (Nth Max)": nth_max_sort,
        "Heapq (Nth Max)": nth_max_heap,
        "Iterative Max (Nth Max)": nth_max_max,
        "Sorting (Nth Min)": nth_min_sort,
        "Heapq (Nth Min)": nth_min_heap,
        "Iterative Min (Nth Min)": nth_min_min
    }

    print(f"Comparing efficiency for finding {n}th maximum and minimum elements:\n")

    for name, func in algorithms.items():
        start = time.time()
        result = func(lst, n)
        end = time.time()
        print(f"{name}: Result = {result}, Time = {end - start:.6f} seconds")

# Example usage
if __name__ == "__main__":
    sample_list = [12, 3, 45, 7, 22, 18, 90, 1, 67, 34]
    n = 3
    compare_algorithms(sample_list, n)
