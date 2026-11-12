x = iter(['a', 'b', 'c'])
print(x)

print(next(x))
print(next(x))
print(next(x))
# print(next(x))

def my_generator():
    i = 0
    print('First Value')
    yield i
    i += 1
    print('Second Value')
    yield i
    i += 1
    print('Last Value')
    yield i
my_gen = my_generator()
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
# print(next(my_gen))


def odd_numbers(numbers):
    for num in range(1, numbers, 2):
        yield num

def square(nums):
    for num in nums:
        yield num ** 2

print(sum(square(odd_numbers(18))))

odd_numbers = (num for num in range(1, 18, 2))

squares = (num ** 2 for num in odd_numbers)

print(sum(squares))