file = open('r.py', 'w')

try:
    file.write('heloo')
finally:
    file.close()

# or
    
with open('r.py', 'w') as file:
    file.write('heloo')