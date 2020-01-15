# I may have used array and list interchangeably in this workshop.
# In python, they're the same thing
# You can't make a list of a fixed size
# You can make a tuple but it's contents cannot be changed
# It can shrink and grow as needed
# You can use some of the array manipulation here with strings as well
# Note: Lists are mutable while strings are immutable
# In python indexing starts at 0

# To find the size of an array, tuple, or string, pass it in the len() method
print(len([1, 2]), len("wasd"))

# Subarrays and subtrings
# You don't need an extra method to access a subarray/substring
# You can use the square bracket indexing
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(arr[1])
print(arr[3:8])
print(arr[3:])
print(arr[:8])
# You can also use negative indexing!!!
# How would you access the last element of an array?
print(arr[len(arr)-1])
# This is also the same equivalent
print(arr[-1]) # No, this won't return an out of bounds error

# And you can combine this with the previous subarray accessing

# How would you make a list that starts at 0 and ends at 7 in one line?
seven = [i for i in range(8)]
print(seven)
