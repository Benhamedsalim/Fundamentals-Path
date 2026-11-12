numbers = [2, 4, 1, 3, 5]
result = 1

for number in numbers:
    result = number * result

print(result)

x = 0
nwe_list_numbers = []
for i in numbers:
    x = i + x
    nwe_list_numbers.append(x)

print(nwe_list_numbers)

numbers = [1, 2, 2, 2, 4, 4, 5, 6, 7, 8, 8]
x = {}
y = []

for number in numbers:
    if number not in x:
        x[number] = 1
    else:
        if x[number] == 1:
            y.append(number)
            x[number] += 1

print(x)
print(y)

words = ['data', 'science', 'machine', 'learning']

char_count = {i: len(i) for i in words}

print(char_count)


numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
groupedNumbers = []
size = 3
for i in range(0 ,len(numbers), size):
    groupedNumbers.append(numbers[i:i+size])

print(groupedNumbers)

grouped_numbers = [numbers[i:i+size] for i in range(0, len(numbers), size)]

print(grouped_numbers)



