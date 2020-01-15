# Here's how python functions are structured
def hello1(name):
    print(f'Hello {name}!')

# This is how you do optional statements
def hello2(name="Gertrude"):
    print(f'Hello {name}')

# How do I restrict variable types for inputs?
# You must assert them.
def hello3(name):
    assert type(name) == str, 'name must be a string'
    print(f'Hello {name}')

# What if I just want to have an empty function that does nothing?
def nothing():
    pass

# How do I make multiple arguments such as in print()?
def sum_of_numbers(*numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum
# The type of *numbers is a tuple


hello1('Gino')
hello2('Gino')
hello2()
# hello3(3)

nothing()

print(sum_of_numbers(1, 2, 3, 5))
