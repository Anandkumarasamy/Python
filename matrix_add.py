
#input of matrix--------
row=int(input("Enter the no of row:"))
col=int(input("Enter the no of colume:"))

print("Enter the elements of matrix1")
matrix1=[[int(input()) for i in range(col)] for j in range(row)]
print("Matrix1:")
for i in range(row):
    for j in range(col):
        print(format(matrix1[i][j],'<3'),end=' ')
    print()

print("Enter the elements of matrix1")
matrix2=[[int(input()) for i in range(col)] for j in range(row)]
print("Matrix2:")
for i in range(row):
    for j in range(col):
        print(format(matrix2[i][j],'<3'),end='')
    print()

#Apply action of matrix

result1=[[0 for i in range(col)] for j in range(row)]
for i in range(row):
    for j in range(col):
        result1[i][j]=matrix1[i][j]+matrix2[i][j]

print("the result of add matrix")
for i in range(row):
    for j in range(col):
        print(format(result1[i][j],'<3'),end='')
    print()

result2=[[0 for i in range(col)] for j in range(row)]
for i in range(row):
    for j in range(col):
        result2[i][j]=matrix1[i][j]-matrix2[i][j]

print("the result of subract matrix")
for i in range(row):
    for j in range(col):
        print(format(result2[i][j],'<3'),end='')
    print()