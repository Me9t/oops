import heapq

# Coin Change Problem (Greedy Approach)
def coin_change_greedy(coins, amount):
    coins.sort(reverse=True)  # Sort coins in descending order
    result = {}
    total_coins = 0

    for coin in coins:
        if amount >= coin:
            count = amount // coin  # Get maximum coins of this denomination
            amount -= count * coin
            result[coin] = count
            total_coins += count

        if amount == 0:
            break

    if amount != 0:
        return "Solution not possible with given denominations"

    return result, total_coins

# File Merging Problem (Greedy Approach using Min-Heap)
def min_file_merge_cost(files):
    heapq.heapify(files)  # Min heap to get smallest files first
    total_cost = 0

    while len(files) > 1:
        # Extract two smallest files
        first = heapq.heappop(files)
        second = heapq.heappop(files)

        merge_cost = first + second
        total_cost += merge_cost

        # Push merged file back into the heap
        heapq.heappush(files, merge_cost)

    return total_cost

# Example Usage
if __name__ == "__main__":
    # Coin Change Example
    coins = [1, 5, 10, 25]
    amount = 63
    print("Coin Change Solution:", coin_change_greedy(coins, amount))

    # File Merging Example
    file_sizes = [4, 8, 6, 12]
    print("Minimum File Merge Cost:", min_file_merge_cost(file_sizes))
