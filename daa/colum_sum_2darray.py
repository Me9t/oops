arr=[[1,2,3], [4,5,6], [7,8,9]]
col_sum=[]
for i in range (len(arr[0])):
    col_sum.append(sum(row[i] for row in arr))
print ("Column sum of array:", col_sum)