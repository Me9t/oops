import threading

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    print(f"Factorial of {n}: {result}")

def reverse(n):
    print(f"Reverse of {n}: {str(n)[::-1]}")

if __name__ == "__main__":
    num = 12
    t1 = threading.Thread(target=factorial, args=(num,))
    t2 = threading.Thread(target=reverse, args=(num,))
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    print("Both threads completed")
