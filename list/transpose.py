'''Write a function that takes a 3x3 matrix (nested list) as input 
and returns its transpose. Print the original and transposed matrices.'''

def transpose(matrix):
    #row (i) is outer loop and column (j) is a inner loop
    transposed = [ [matrix[j][i] for j in range(len(matrix[0]))]for i in range(len(matrix))]
    return transposed

def trans(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[j][i],end=" ")
        print()

matrix = [
    [1,2,3],
    [3,4,5],
    [6,7,8],
]


for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j],end=" ")
    print()

print("transpose")
transposed = transpose(matrix)

for i in range(len(transposed)):
    for j in range(len(transposed[0])):
        print(transposed[i][j],end = " ")
    print()

print("tranpose")
trans(matrix)
