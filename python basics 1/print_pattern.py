no_rows = int(input("Enter The Numeber of Rows :"))
'''1]'''
# for row in range( 1, no_rows + 1 ):
#     for column in range( 1,row+1):
#         print("*", end = " ")
#     print()

'''2]'''
# for row in range( no_rows - 1, 0, -1 ):
#     for column in range( 1,row+1):
#         print("*", end = " ")
#     print()

'''3]'''
for row in range( 1, no_rows + 1 ):
    for column in range( 1,row+1):
        print("{0}{1}".format(row, column), end = " ")
    print()

'''4]'''
for row in range( no_rows - 1, 0, -1 ):
    for column in range( 1,row+1):
        print("{0}{1}".format(row, column), end = " ")
    print()