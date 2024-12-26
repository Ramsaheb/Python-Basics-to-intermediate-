# def factorial(n):
#     if type(n) is int and n >= 0:
#         if n == 0:
#             return 1
#         else:
#             return n * factorial(n - 1)
        
#     else:
#         raise TypeError('n must be an integer or zero')

# print(factorial(int(input()))) 


def polynomial_creator(a, b, c):
    def polynomial(x):
        return a * x ** 2 + b * x + c
    return polynomial
p1 = polynomial_creator(1, 2, 3)
p2 = polynomial_creator(-1, 2, 3)

