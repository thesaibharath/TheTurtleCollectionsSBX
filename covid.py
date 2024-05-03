import turtle

t = turtle.Turtle()
s = turtle.Screen()
t.speed(0)
s.bgcolor("black")
t.pencolor("red")
a,b = 0,0
while True:
	t.forward(a)
	t.right(b)
	a+=3
	b+=1
	if b == 200:
		break
		t.hideturtle()
turtle.done()