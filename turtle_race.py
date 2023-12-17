# Import necessary modules
from turtle import Turtle, Screen
import random

# Initialize variables and lists
is_race_on = False
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

# Set up the turtle screen
screen = Screen()
screen.setup(width=500, height=400)

# Get user input for betting on a turtle
user_input = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_input)
all_turtles = []

# Create turtle objects for each color and position them on the starting line
for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[i])
    all_turtles.append(new_turtle)

# If user input is provided, start the race
if user_input:
    is_race_on = True

# Simulate the race until a turtle reaches the finish line
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            # Determine if the user's bet matches the winning turtle
            if winning_color == user_input:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        # Move each turtle forward by a random distance
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

# Close the turtle screen on click
screen.exitonclick()
