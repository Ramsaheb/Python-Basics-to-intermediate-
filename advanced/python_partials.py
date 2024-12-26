# def power(base, exponent):
#     print('{} to the power of {}'.format(base, exponent, base ** exponent))
#     return base ** exponent

# def square(base):
#     return power(base, 2)

# def cube(base):
#     return power(base, 3)

# print(power(2, 3))
# print(square(4))


from functools import partial

# square = partial(power, exponent = 1000)
# print(square(2))

def f(a, b, c, x):
    return 100*a + 10*b + 10*c + x

new = partial(f, 2, 3, 4)
print(new(10))