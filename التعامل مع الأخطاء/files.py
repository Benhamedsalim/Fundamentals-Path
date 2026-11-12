with open('file.txt', 'r') as f, open('file2.txt', 'w') as f2:
    f_lines = f.resd()
    f2.write(f_lines)

with open('ball.png', 'rb') as f:
    print(f.read(8))


# with open('file.txt', 'a') as f:
#     f.write('Hello! This text is written by Python\n')
#     f.write('Python is a great programming language.')

# f = open('file.txt', 'w')

# f.write('Hello! This text is written by Python\n')
# f.write('Python is a great programming language.')

# f.close()

# f = open('file.txt', 'r')

# for line in f:
#     print(line, end = ' ')

# f.close()
with open('file.txt') as f:
    print(f.read)