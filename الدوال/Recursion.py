books = ['Effective Python', 'Byte of Python', 'Python Essential Reference', 'Think Python', 'Python Cookbook']

def print_books(list):
    if len(list) == 0:
        return
    else:
        print(list[0])
        return print_books(list[1:]) 

print_books (books)


data = [['Effective Python', 'Byte of Python', 'Python Essential Reference'], 44, 12, 'Python Cookbook', ('Books', 'Websites')]

def print_data(data):
    if not data: return
    if (type(data[0]) == list or type(data[0]) == tuple):
        print_data(data[0])
    else:
        print(data[0])
        print_data(data[1: ])

print_data(data)