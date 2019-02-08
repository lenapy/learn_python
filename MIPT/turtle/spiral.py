import turtle
# теория https://ru.wikipedia.org/wiki/%D0%90%D1%80%D1%85%D0%B8%D0%BC%D0%B5%D0%B4%D0%BE%D0%B2%D0%B0_%D1%81%D0%BF%D0%B8%D1%80%D0%B0%D0%BB%D1%8C
turtle.shape('turtle')
z = 3
for _ in range(10):
	for _ in range(25):
		turtle.forward(z)
		turtle.left(20)
	z+=1