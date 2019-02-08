# каскадное присваевание
a = b = c = 1
b = 2
print(a, b, c)

x = y = z = [1, 1, 1]
x.append(2)
print(x, y, z)

# множественное присваивание
k, l, m = 1, 2, 3

for i in range(20, 10, -2):
	print(i)

i = 20
while i > 10:
	print(i)
	i -= 2