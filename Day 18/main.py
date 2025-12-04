# ===========================================
# Spot Painting Code -> Paints color dots
# ===========================================

import turtle as t
import random
from color_data import color_list

timmy = t.Turtle()
t.colormode(255)
timmy.speed("fastest")
timmy.teleport(-250, -250)
number_of_dots = 101


for count_dots in range(1, number_of_dots):
    timmy.dot(20,random.choice(color_list))
    timmy.penup()
    timmy.forward(50)
    # Repositions Timmy to start from beginning
    if count_dots % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

# To lock screen, to see output
screen = t.Screen()
screen.exitonclick()
