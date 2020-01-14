# strings are immutable
a = [1, 2, 3, 4]
a[0] = 20
# this prints what is expected
print(a)

s = "Hello"
print(s[0])
s[0] = "h"
# What will happen?
print(s)