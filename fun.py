import turtle
import math

# Set up the Turtle screen
screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Spiral Animation")

# Create a Turtle object
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.width(2)

# Function to draw a spiral
def draw_spiral():
    for i in range(100):
        radius = i * 5
        angle = 0.1 * i
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        pen.goto(x, y)

# Function to animate the spiral
def animate_spiral():
    angle = 0
    while True:
        pen.clear()
        draw_spiral()
        angle += 0.1  # Adjust the rotation speed as needed
        pen.right(angle)

# Main function
def main():
    draw_spiral()  # Draw the initial spiral
    animate_spiral()  # Start the animation
    turtle.done()

if __name__ == "__main__":
    main()
