import turtle
from tkinter import messagebox, simpledialog, Tk
from easygui import *

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    size = 60
    # Make a new turtle
    t = turtle.Turtle()
    # Ask the user what shape they want to draw and store it in a variable
    choices1 = ["Square","Triangle","Circle"]
  
    # creating a button box
output = choicebox("Do you want to draw a square, circle, or triangle?", "Shape selector", choices1)
    # Draw the shape requested by the user using if-elif-else statements
if output == "Square":
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)
elif output == "Triangle":
    for i in range(3):
        turtle.forward(size)
        turtle.left(360/3)
elif output == "Circle":
    turtle.circle(size,steps = 100)    
# Call the turtle .done() method
