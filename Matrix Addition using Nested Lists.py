A = [[1, 2, 3],
     [4, 5, 6]]

B = [[7, 8, 9],
     [10,11, 12]]

res = []
for i in range(len(A)):
    row = []   
    for j in range(len(A[0])):
        row.append(A[i][j] + B[i][j])       
    res.append(row)
print("Result Matrix:")

for row in res:
    print(row)