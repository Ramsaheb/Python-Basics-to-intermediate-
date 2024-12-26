n = int(input("ENTER NO. OF ROW AND COLUMN : "))
a = [[0] * n for _ in range(n)]

print("ENTER MATRIX ELEMENT (separated by spaces): ")
for i in range(n):
    row_input = input().split()
    for j in range(n):
        a[i][j] = int(row_input[j])

print("GIVEN MATRIX IS : ")
for i in range(n):
    for j in range(n):
        print(a[i][j], end=" ")
    print()


for k in range(n):
    for i in range(n):
        for j in range(n):
            if a[i][j] > a[i][k] + a[k][j]:
                a[i][j] = a[i][k] + a[k][j]

print("YOUR MATRIX IS :")
for i in range(n):
    for j in range(n):
        print(a[i][j], end="\t")
    print()
