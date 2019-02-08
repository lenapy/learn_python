import turtle

turtle.shape('turtle')
x = -5
y = -5
z = 10

for _ in range(10):
	for _ in range(4):
		turtle.forward(z)
		turtle.left(90)
	z += 10
	turtle.penup()
	turtle.goto(x, y)
	turtle.pendown()
	y -= 5
	x -= 5




