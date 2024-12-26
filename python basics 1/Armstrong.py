a = int(input("Enter the number :"))

# for i  in range(1001) :
i = a
result = 0
n = len(str(i))

while (i!=0) :
        digit = i % 10
        result += digit ** n
        i = i // 10

if a == result :
        print("the entered number is Armstrong")

else :
         print("the entered number is not an Armstrong")