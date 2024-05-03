import turtle

# Set up the Turtle screen
screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Celestial Mandala")

# Create a Turtle object
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.width(1)

# Function to draw a single petal
def draw_petal(size):
    for _ in range(36):
        pen.forward(size)
        pen.left(160)
        pen.forward(size)
        pen.left(140)

# Function to draw a full flower with petals
def draw_flower(size):
    for _ in range(6):
        draw_petal(size)
        pen.left(60)

# Function to draw the celestial elements
def draw_celestial_elements():
    for _ in range(36):
        pen.forward(200)
        pen.backward(200)
        pen.left(10)

# Main function to draw the complete design
def main():
    pen.penup()
    pen.goto(0, -300)
    pen.pendown()
    pen.color("yellow")
    pen.begin_fill()
    draw_flower(100)
    pen.end_fill()
    pen.penup()
    pen.goto(0, 0)
    pen.pendown()
    pen.color("white")
    draw_celestial_elements()
    pen.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
