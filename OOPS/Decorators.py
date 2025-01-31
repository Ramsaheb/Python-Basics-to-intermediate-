# def greet(fx):
#     def fn(*args, **kwargs):
#         print('good morning')
#         fx()
#         print('good night')
#     return fn
# @greet
# def hello():
#     print('hello')

# def add(a, b):
#     print(a + b)

# hello()
# add(1, 2)


import logging

def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated

@log_function_call
def my_function(a, b):
    return a + b

my_function(5, 6)