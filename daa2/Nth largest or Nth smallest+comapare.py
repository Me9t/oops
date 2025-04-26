import heapq
import time

# Function to find the Nth maximum element using heapq.nlargest
def nth_max_heap(lst, n):
    return heapq.nlargest(n, lst)[-1]  # Get the Nth largest using nlargest

# Function to find the Nth minimum element using heapq.nsmallest
def nth_min_heap(lst, n):
    return heapq.nsmallest(n, lst)[-1]  # Get the Nth smallest using nsmallest

# Function to find the Nth maximum element using max function iteratively
def nth_max_max(lst, n):
    temp_lst = lst.copy()  # Avoid modifying the original list
    for _ in range(n - 1):
        temp_lst.remove(max(temp_lst))  # Remove the max N-1 times
    return max(temp_lst)

# Function to find the Nth minimum element using min function iteratively
def nth_min_min(lst, n):
    temp_lst = lst.copy()  # Avoid modifying the original list
    for _ in range(n - 1):
        temp_lst.remove(min(temp_lst))  # Remove the min N-1 times
    return min(temp_lst)

# Function to compare efficiency of algorithms
def compare_algorithms(lst, n):
    # Define the algorithms to compare
    algorithms = {
        "Heapq (Nth Max)": nth_max_heap,
        "Iterative Max (Nth Max)": nth_max_max,
        "Heapq (Nth Min)": nth_min_heap,
        "Iterative Min (Nth Min)": nth_min_min
    }

    print(f"Comparing efficiency for finding {n}th maximum and minimum elements:\n")

    # Iterate through the algorithms and measure time taken
    for name, func in algorithms.items():
        start = time.time()  # Start timing
        result = func(lst, n)  # Call the function
        end = time.time()  # End timing
        print(f"{name}: Result = {result}, Time = {end - start:.6f} seconds")

# Example usage
if __name__ == "__main__":
    sample_list = [12, 3, 45, 7, 22, 18, 90, 1, 67, 34]
    n = 3  # For example, find the 3rd largest or smallest
    compare_algorithms(sample_list, n)
