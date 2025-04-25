def factorial_recursive(n):
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)

def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, auxiliary, target, source)

# Factorial
print("Factorial of 5 (Recursive):", factorial_recursive(5))
print("Factorial of 5 (Iterative):", factorial_iterative(5))

# Fibonacci
print("Fibonacci of 7 (Recursive):", fibonacci_recursive(7))
print("Fibonacci of 7 (Iterative):", fibonacci_iterative(7))

# Tower of Hanoi
print("Tower of Hanoi with 3 disks:")
tower_of_hanoi(3, 'A', 'C', 'B')
