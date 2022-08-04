# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.

#Area = πr^2
#Circumference = 2πr 
import math
from tkinter import messagebox, simpledialog, Tk
from tkinter import *
import tkinter as tk
from easygui import *

window = Tk()
window.withdraw()
radius = simpledialog.askfloat("Circle Calculator","What is the radius of the circle?")
choices1 = ["Area","Circumference"]
  
    # creating a button box
output = choicebox("Do you want to calculate the area, or circumference of a circle?", "Circle Calculator", choices1)
if output == "Area":
    messagebox.showinfo("Circle Calculator", "The area of this circle is " + str(math.pi*radius**2))
elif output == "Circumference":
    messagebox.showinfo("Cicle Calculator", "The circumference of this circle is " + str(2*math.pi*radius))