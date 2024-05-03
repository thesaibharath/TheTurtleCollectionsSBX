import turtle

t = turtle.Turtle()
s = turtle.Screen()
t.speed(0)
s.bgcolor("black")
t.pencolor("green")
a,b = 0,0
while True:
	t.forward(b)
	t.right(a)
	a+=10
	b+=0.1
	if b == 200:
		break
		t.hideturtle()
turtle.done()