# try:
#     with open('my_file.txt') as file:
#         data = file.read()

# except:
#     print('I cannot find the file.')

# try:

#     with open('my_file.txt', 'w') as file:
#         ## data = file.read()
#         x = 6
#         y = 3

#         result =(x+y)/(x-y)

#         file.write(f'The result is {result}')
# except FileNotFoundError as error:
#     print(error)
# except ZeroDivisionError as error:
#     print(error)
# else:
#     print('The result was written to the file')
# finally:
#     print('Code execution was finished')

# try:

#     x = 6
#     y =3
#     print(x/(x-y))

# except:
#     print('Did you divide by zero?')


# raise Exception('This is an exception')
# print(3/0)

class TooOldError(Exception):
    def __init__ (self, message):
        self.message = message

    def __str__ (self):
        return self.message

class TooYoungError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

age = int(input('Enter your age: '))
if age < 15: raise TooYoungError(f'Sorry, but you are {age} years old. You are too young to sign in.')
if age > 48: raise TooOldError(f'Sorry, but you are {age} years old. You are too old to sign in.')