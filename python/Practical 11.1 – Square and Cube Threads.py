import threading

def square(num):
    print(f"Square of {num}: {num**2}")

def cube(num):
    print(f"Cube of {num}: {num**3}")

if __name__ == "__main__":
    num = 5
    t1 = threading.Thread(target=square, args=(num,))
    t2 = threading.Thread(target=cube, args=(num,))
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    print("Both threads completed")
