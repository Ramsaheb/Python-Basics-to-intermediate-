def LCS_LENGTH(x, y):
    m = len(x)
    n = len(y)
    b = [[None] * (n + 1) for _ in range(m + 1)]
    c = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = 'D'
            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                b[i][j] = 'U'
            else:
                c[i][j] = c[i][j - 1]
                b[i][j] = 'L'
    return c, b

def PRINT_LCS(b, x, i, j):
    if i == 0 or j == 0:
        return
    elif b[i][j] == 'D':
        PRINT_LCS(b, x, i - 1, j - 1)
        print(x[i - 1], end='') 
    elif b[i][j] == 'U':
        PRINT_LCS(b, x, i - 1, j)
    else:
        PRINT_LCS(b, x, i, j - 1)

x = 'ABACAD'
y = 'BAACBD'
c, b = LCS_LENGTH(x, y)
print('LENGTH OF LCS : ', c[len(x)][len(y)])
print('LCS : ', end='')
PRINT_LCS(b, x, len(x), len(y))
