numbers = [1, 2, 3, 4, 5]
def get_squares(x):
    return x**2

squares = map(get_squares, numbers) #تعيد الدالة map() مكررًا يطبق الدالة المعطاة على كل عنصر من عناصر الكائن الممرر.
print(list(squares))


temps= [("Damascus",29), ("Cairo", 36), ("Baghdad", 44), ("Riyadh",40), ("Beirut", 34), ("Tunis", 30)]

# F = 1.8*C + 32

def C_to_F(item):
    return  item[0], (1.8)*item[1] + 32

f_temps = list(map(C_to_F, temps))

print(f_temps)

f_temps= list(map(lambda item: (item[0], (1.8)*item[1]+32), temps))

print(f_temps)

f_temps = []
for temp in temps:
    f=(1.8) * temp[1] + 32
    f_temps.append((temp[0], f))

print(f_temps)


Languages = [('C', 1972), ('C++', 1985), ('Java', 1995), ('JavaScript', 1995), ('PHP', 1994), ('Python', 1991)]

def old(item):
    return item[1] < 1990

old_languages = filter(old, Languages)
print(list(old_languages))

def find(iterable, text):
    def finder(lang):
        for i in lang:
            if str(i).startswith(text):
                return True
            return False
    return list(filter(finder, iterable)) #ترشح  الدالة filter() عناصر كائن قابل للتكرار.
results = find(Languages, 'J')

print(results)

results = find(Languages, 'PHP')

print(results)


from functools import reduce
#تستخدم الدالة ()reduce لتطبيق دالة مُحددة على جميع عناصر كائن قابل للتكرار.

numbers = [1, 2, 3, 4, 5, 6]

def add(x, y):
    return x + y

print(reduce(add, numbers))

numbers = [33, 51, 94, 11, 40, 83]
print(max(numbers))
max_number = reduce(lambda x, y: x if x > y else y, numbers)

print(max_number)
