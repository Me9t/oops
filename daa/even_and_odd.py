# Count even and odd numbers in a list
list1 = [10, 21, 4, 45, 6, 93, 1]
even_count, odd_count = 0, 0

for num in list1:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers in the list:", even_count)
print("Odd numbers in the list:", odd_count)
