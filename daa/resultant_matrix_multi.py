mat1 = [[1,2], [3,4]]
mat2 = [[5,6], [7,8]]
result = [[0,0],[0,0]]
for i in range (len(mat1)):
    for j in range (len(mat2[0])):
        for k in range (len(mat2)):
            result[i][j] += mat1 [i][k]*mat2[k][j]

print("Resultant matrix after multipication:", result)