"""A tuple is a sequence of variables which itself is immutable.
 That means that a tuple has items in an ordering, but that it cannot be changed once created."""

x = (1, 'a', 2, 'b')
print(type(x))

"""Lists are very similar, but they can be mutable, 
so you can change their length, number of elements, and the element values."""

y = [1, 'a', 2, 'b']
y.append(3)
print(type(y))

for item in y:
	print(item)

i = 0
while i != len(y):
	print(y[i])
	i += 1

y1 = [1, 2] + [3, 4] # y1 = [1, 2, 3, 4]
print(y1)

y2 = 1 in [1, 2, 3] # y = True
print(y2)

st = "This is string"
print(st[0])
print(st[0:2])
print(st[-1])
print(st[:3])
print(st[4:])

s = "Dr. Christopher Brooks"
print(s[4: 15])

""" Dictionaries are similar to lists and tuples in that they hold a collection of items, 
but they're labeled collections which do not have an ordering. 
This means that for each value you insert into the dictionary, 
you must also give a key to get that value out. In other languages the structure is often called a map."""

sales_record = {
'price': 3.24,
'num_items': 4,
'person': 'Chris'}


""" In Python you can have a sequence. That's a list or a tuple of values, 
and you can unpack those items into different variables through assignment in one statement."""

z = ('a', 'b', 'c')
a, b, c = z
print(a,  b, c)