import time

def linear_search(arr,x):
    for i in range(len(arr)):
        if arr[i]==x:
            return i
    return -1

def binary_search(arr,x):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]<x:
            low = mid+1
        elif arr[mid]>x:
            high =mid-1
        else:
            return mid
        
    return -1
        
arr=[2,4,6,8,10,14,16,17,19,20,21,25,28,29] 

start=time.time()  
result =linear_search(arr,28)
end=time.time()
print(f"Linear Search took {(end - start)*1000:.6f} ms. Found at index: {result}")

    
start=time.time()  
result =binary_search(arr,28)
end=time.time()
print(f"Linear Search took {(end - start)*1000:.6f} ms. Found at index: {result}")