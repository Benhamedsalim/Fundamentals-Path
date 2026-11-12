def my_function():
    print('Hello World!')

my_function()

def sum():
    print(3)
    print(4)
    return
    print(3 + 40)

sum()

def get_age():
    age = int(input("Enter your age: "))
    if age < 0 :
        return
    elif age > 120:
        return
    print(age)

get_age()

def degree():
    return 40

x = degree()
print(x)

def temp_scales():
    return ['Celsius', 'Fahrenheit', 'Kelvin']

scale = temp_scales()[2]

print(scale)