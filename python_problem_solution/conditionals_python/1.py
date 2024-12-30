age = int(input("Tell me your age : "))
# day1 = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
day =input("Enter the day : ")

if age >= 18 and day != 'w':
    print("please pay 12$ for ticket")

elif age < 18 and day != 'w':
    print("please pay 8$ for ticket")

elif age >= 18 and day == 'w': 
    print("Sir you got an discount of \" 2$ \" now just pay \" 10$ \"")

elif age < 18 and day == 'w':
    print("Sir you got an discount of \" 2$ \" now just pay \" 6$ \"")