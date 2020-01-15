# char type does nont exist in python
# strings are made up of smaller string
# I know, it's weird
# strings are immutable

# How do I format strings?
# There are many ways to do it in python
# For example, you can simply add them together
hello = "Hello "
world = "World!"
print(hello + world)

# A better way of doing it is with f-strings
prompt = "How are you? My name is"
name = "Boaty McBoatface"
print(f'{prompt} {name}')

# How do you make all upper/lower case?
a = 'HEllo'
print(a.lower())
print(a.upper())

# split
# What if I wanted to split the string at some pattern?
print("split this\noof".split(' '))
print("This workshop is boring".split('s', 2))
print("Lorem ipsum blabla other words".split())

# join
a = "words random boat yeet"
print(a.split())
print('-'.join(a.split()))
