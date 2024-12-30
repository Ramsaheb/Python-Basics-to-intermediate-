# def circumference_of_circle(radius):
#     return 2 * 3.14 * radius

# def area(radius):
#     return 3.14 * radius * radius

# r = int(input('enter radius : '))
# print(circumference_of_circle(r))
# print(area(r))


import math
def circle_stats(radius):
    area = math.pi * radius *2
    circumference = math.pi * radius * radius
    return circumference, area
a, b = circle_stats(5)
a_formetted = "{:.2f}".format(a)
b_formetted = "{:.2f}".format(a)
print('circumference_of_circle : ', a_formetted, 'radius : ', b_formetted)