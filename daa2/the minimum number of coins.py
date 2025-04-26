# Coin Change Problem (Greedy Approach)
def coin_change_greedy(coins, amount):
    coins.sort(reverse=True)  # Sort coins in descending order
    result = {}
    total_coins = 0

    for coin in coins:
        if amount >= coin:
            count = amount // coin  # Maximum coins of this type
            amount -= count * coin
            result[coin] = count
            total_coins += count

        if amount == 0:
            break

    if amount != 0:
        return "Solution not possible with given denominations"

    return result, total_coins

# Example usage for Coin Change
if __name__ == "__main__":
    coins = [1, 5, 10, 25]
    amount = 63
    print("Coin Change Solution:", coin_change_greedy(coins, amount))
