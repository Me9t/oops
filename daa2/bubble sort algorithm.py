def bubblesort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(n-i-1): 
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
my_array=[1,7,9,4,7]
print(f"og array{my_array}")
sorted=bubblesort(my_array)
print(f"sorted array{sorted}")
