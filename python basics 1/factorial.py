# import math
# fact = int(input("enter the number :"))
# result = math.factorial(fact)
# print("the factorial of",fact ,"=",result)


# by using loop

N = int(input("enter the number : "))
result = 1
for i in range(N, 0 , -1) :
    if i != 0 :
        result = result * i

print(result)

    
      
        