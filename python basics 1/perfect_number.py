# n = int(input("enter the number : "))
lower = int(input(""))
upper = int(input(""))

for i in range(lower, upper + 1 ) :
    result = 0
    for j in range(1, i):
        if( i% j == 0):
            result = result + j
    if(result == i):
        print("the number is perfect : ", i)



