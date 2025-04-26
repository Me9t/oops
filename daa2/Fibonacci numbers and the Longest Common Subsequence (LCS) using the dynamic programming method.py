# Fibonacci Series using Dynamic Programming

# Memoization (Top-Down)
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

# Tabulation (Bottom-Up)
def fibonacci_tab(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

# Longest Common Subsequence (LCS) using Dynamic Programming
def lcs(X, Y):
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

# Example Usage
if __name__ == "__main__":
    # Fibonacci Example
    n = 10
    print("Fibonacci (Memoization):", fibonacci_memo(n))
    print("Fibonacci (Tabulation):", fibonacci_tab(n))

    # LCS Example
    str1 = "AGGTAB"
    str2 = "GXTXAYB"
    print("Longest Common Subsequence Length:", lcs(str1, str2))
