# def cube(x):
#     return x ** 3


#Boring zindagi

# newl = []
# for i in l:
#     newl.append(cube(i))
# print(newl)

#mentos zindagi

#print(list(map(cube, l)))


#FILTER
# def filter_func(a):
#     return a > 4
# newl = filter(filter_func, l)
# print(list(newl))

#REDUCE
l = list(map(int, input()))
from functools import reduce
newll = reduce(lambda x, y : x + y, l)
print(newll)


