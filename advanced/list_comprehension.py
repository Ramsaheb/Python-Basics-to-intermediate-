# name = ['ram', 'sham', 'dham', 'shu']
# new_list = [_ for _ in name if 'a' in _]
# print(new_list)


# h_letters = [letter for letter in 'human']
# print(h_letters)

# first_ten_even_number = [x for x in range(1, 1111) if x % 2 == 0 ][:10]
# first_ten_even_number = ['even' if x % 2 == 0 else 'odd' for x in range(10)]
# print(first_ten_even_number)

# def square(x):
#     return x ** 2

# squares = [square(x) for x in range(100000000)]
# print(squares)

text = "hi i am ramsaheb prasad,nice to meet you..."
unique_vowels = {each_letter for each_letter in text if each_letter in 'aeiou'}
# print(unique_vowels)

square = {i : i ** 2 for i in range(10)}
print(square)