def print_info(name, age, weight):
    print(f'Name: {name}, Age: {age}, Weight: {weight} kg')

print_info(name='Saeed', age=33, weight=88)
print_info(age=33, name='Saeed', weight=88)
print_info('Saeed', age=33, weight=88)
print_info('Saeed', 33, weight=88)


def printIfruits(*fruits):
    for fruit in fruits:
        print(f'I like {fruit}')

printIfruits('Apple', 'Orange', 'Banana', 'Grapes', 'Pear')

def weather(** kwargs):
    print(kwargs)

weather(location='Baghdad', temperature=40, condition='Sunny', wind_speed=3)