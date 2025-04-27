import threading

def sum_squares(start, end):
    total = sum(i**2 for i in range(start, end+1))
    print(f"Sum of squares ({start}-{end}): {total}")

def sum_cubes(start, end):
    total = sum(i**3 for i in range(start, end+1))
    print(f"Sum of cubes ({start}-{end}): {total}")

if __name__ == "__main__":
    start, end = 1, 5
    t1 = threading.Thread(target=sum_squares, args=(start, end))
    t2 = threading.Thread(target=sum_cubes, args=(start, end))
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()
    
    print("Both threads completed")
