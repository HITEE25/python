'''Create a nested list representing a 3x3 matrix and print the 
matrix.Access and print the element at the second row and third column'''

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]
]
#col => print(len(matrix[0]))
print(len(matrix[0]))
#row => print(len(matrix))
print(len(matrix))
#row size
for i in range(len(matrix)):
    #col size
    for j in range(len(matrix[0])):
        print(matrix[i][j] ,end=" ")
    print()

print(matrix[1][2])

