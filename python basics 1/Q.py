# 123 = 1+2+3 = 6
    
n = int(input("enter the number"))  
sum = 0
while n != 0 :
    dig = n%10
    sum += dig
    n = n // 10
   
print(sum)




