def factorial_recursive(n):
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Factorial
print("Factorial of 5 (Recursive):", factorial_recursive(5))
print("Factorial of 5 (Iterative):", factorial_iterative(5))
