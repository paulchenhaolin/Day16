# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import turtle

import another_module
print(another_module.another_variable)

from turtle import Turtle, Screen
timmy = Turtle()
print(timmy)  # printing an object
timmy.shape("turtle")
timmy.color("coral")
timmy.forward(100)
my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()  # only finish it after you click it
