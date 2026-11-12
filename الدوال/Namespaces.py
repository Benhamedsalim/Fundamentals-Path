x = 100
def add(y):
    z = x + y
    return z

print(add(50))

x = 100

def print_number():
    global x
    print(x)

print_number ()

def outer():
    x = 100

    def inner():
        nonlocal x
        x = 300

    inner()

    print(x)

outer()