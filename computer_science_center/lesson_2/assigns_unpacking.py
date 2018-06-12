acc = []

seen = set()

(acc_1, seen_1) = ([], set()) # справа может быть любой итератор

x, y, z = [1, 2, 3]

x1, y1, z1 = {1, 2, 3} # unordered

x2, y2, z2 = "xyz"

rectangle = (0, 0), (4, 4)
(x_1, y_1), (x_2, y_2) = rectangle

# unpacking

first, *rest = range(1, 5)
print(first) # prints 1
print(rest) # prints [2, 3, 4]

f, *r, last = range(1, 5)
print(f) # prints 1
print(r) # prints [2, 3]
print(last) # prints 4

import dis

print(dis.dis("first, *rest, last = ('a', 'b', 'c')"))
""" 1           0 LOAD_CONST               4 (('a', 'b', 'c'))
              2 EXTENDED_ARG             1
              4 UNPACK_EX              257
              6 STORE_NAME               0 (first)
              8 STORE_NAME               1 (rest)
             10 STORE_NAME               2 (last)
             12 LOAD_CONST               3 (None)
             14 RETURN_VALUE"""

# присваивание работает слева на право

x_, (x_, y_) = 1, (2, 3)
print(x_) # prints 2
print(y_) # prints 3




