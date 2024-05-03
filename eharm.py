import turtle

# Set up the Turtle screen
screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Eternal Harmony")

# Create a Turtle object
pen = turtle.Turtle()
pen.speed(10)
pen.color("white")
pen.width(1)

# Function to draw the complex pattern
def draw_pattern(size, depth):
    if depth == 0:
        return
    else:
        for _ in range(6):
            pen.forward(size)
            draw_pattern(size / 3, depth - 1)
            pen.backward(size)
            pen.left(60)

# Main function to draw the complete design
def main():
    pen.penup()
    pen.goto(-150, 150)
    pen.pendown()
    draw_pattern(300, 4)
    pen.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
