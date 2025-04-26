import heapq

# File Merging Problem (Greedy Approach using Min-Heap)
def min_file_merge_cost(files):
    heapq.heapify(files)  # Convert list to min-heap
    total_cost = 0

    while len(files) > 1:
        first = heapq.heappop(files)
        second = heapq.heappop(files)

        merge_cost = first + second
        total_cost += merge_cost

        heapq.heappush(files, merge_cost)

    return total_cost

# Example usage for File Merge
if __name__ == "__main__":
    file_sizes = [4, 8, 6, 12]
    print("Minimum File Merge Cost:", min_file_merge_cost(file_sizes))
