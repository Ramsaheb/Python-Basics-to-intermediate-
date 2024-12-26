def do(fx, value):
    return 10 + fx(value)

cube = lambda x : x ** 3

print(do(cube, 4))