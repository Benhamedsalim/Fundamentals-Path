class MyType:
    def __len__ (self):
        return 1000

my_type = MyType()
print(len(my_type))

# it duplicates the given float number.
def duplicate(value: float) -> float:
    """
    it duplicates the given float number.
    """
    return value * 2 # return the duplicate value

print(duplicate('5'))