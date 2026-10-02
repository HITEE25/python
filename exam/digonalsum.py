def DiagCalc(M):
    n = len(M)
    left_diag = 0
    right_diag = 0

    for i in range(n):
        left_diag += M[i][i]
        right_diag += M[i][n-i-1]

    print(left_diag)
    print(right_diag)

M = [[1,2,3],
     [3,4,5],
     [6,7,81]]

DiagCalc(M)