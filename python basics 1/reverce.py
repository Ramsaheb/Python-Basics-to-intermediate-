def reverse(string):
    reverse_string = ''
    for i in string :
        reverse_string = i + reverse_string
    print('reverced string is :',reverse_string)

string = input('enter the string :')
print('entered string',string)
reverse(string)
