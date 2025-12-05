import random
from turtle import Turtle, Screen

screen = Screen()

is_race_on = False
screen.setup(width=500, height= 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Choose a color: ")

colors = ["purple", "indigo", "blue", "green", "yellow", "red"]
y_positions = [-70, -30, 10, 50, 90, 130]
print(user_bet)
all_turtles = []
for i in range(0, len(y_positions)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y = y_positions[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle won the race.")
            else:
                print(f"You've lost! The {winning_color} turtle won the race.")
            break

screen.exitonclick()
