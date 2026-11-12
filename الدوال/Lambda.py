def my_function(a):
    return a

add = lambda a, b: a + b
print(add(100, 300))

student_name = lambda first_name, last_name: f"Student's Name: {first_name.title()} {last_name.title()}"

print(student_name('Ahmed', 'Saeed'))

ids = ['id1','id108', 'id2', 'id22', 'id4', 'id40']

ids.sort(key = lambda x: int(x[2:]))
print(ids)

def sort_key(x):
    return int(x[2:])

ids.sort(key = sort_key)
print(ids)