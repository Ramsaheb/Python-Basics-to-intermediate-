# file = open('a.txt', 'r')
# i = 0
# while True:
#     i += 1
#     line = file.readline()
#     if not line:
#         break
#     m1 = line.split(',')[0]
#     m2 = line.split(',')[1]
#     m3 = line.split(',')[2]
#     print(f'Marks of student {i} is in english is: {m1}')
#     print(f'Marks of student {i} is in maths is: {m2}')
#     print(f'Marks of student {i} is in bio is: {m3}')

#     print(line)


f = open('myfile.txt', 'w')
lines = ['line1\n', 'line2\n', 'line3']
f.writelines(lines)
f.close()