import math

print(math.floor(4.6))
print(math.ceil(4.1))
print(round(4.9))
print(round(4.5))
print(math.exp(2.4))

print(math.log(1000))

print(math.log(1000, 10))
print(math.log10(1000))

print(math.pow(2, 5))
print(2**5)
print(math.sqrt(23123))
print(math.pi)
print(math.e)
print(1.1 + 2.2)
print(0.1 + 0.1 + 0.1 == 0.3)
print(0.1 + 0.1 + 0.1 - 0.3)

import decimal

decimal1 = decimal.Decimal(3)

decimal2 = decimal.Decimal('3.14')

decimal3 = decimal.Decimal(2/4)

print(decimal1 + decimal2)

print(decimal2 - decimal2)
print(decimal3.sqrt())

import random

print(random.random())
print(random.random())
print(random.random())
print(random.random())
print(random.random())
print(random.random())

print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))
print(random.randint(1, 10))

print(random.randrange(10))
print(random.randrange(10))
print(random.randrange(10))
print(random.randrange(10))
print(random.randrange(10))
print(random.randrange(10))
print(random.randrange(10))
names = ['Sara', 'Nada', 'Tawfeeq', 'Mohsen', 'Jalal', 'Saeed', 'Zohoor']

print(random.choice(names))
print(random.choice(names))
print(random.choice(names))
print(random.choice(names))
print(random.choice(names))
print(random.choice(names))

print(random.choices(names, k=3))

print(names)
random.shuffle(names)
print(names)