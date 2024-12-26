# def outerfunction(text):
#     text = text

#     def innerfunction():
#         print(text)

#     innerfunction()

# outerfunction('hellooo')

def outerfunction(text):
    text = text

    def innerfunction():
        print(text)

    return innerfunction

my_func = outerfunction('hellooo')
# print(my_func)
my_func()