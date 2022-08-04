from tkinter import *
import tkinter as tk
from easygui import *

window_width = 600
window_height = 600

root = tk.Tk()


# 1. Ask the user what color tomato they would like and save their response
#    You can give them up to three choices
choices1 = ["Red","Blue","Green"]
  
    # creating a button box
output = choicebox("What color tomato do you want", "questions", choices1)
# 2. Use if-else statements to draw the tomato in the color that they chose
#    You can modify the code below or draw your own tomato
canvas = tk.Canvas(root, width=window_width, height=window_height, bg="#DDDDDD")
canvas.grid()

if output == "Red":
    canvas.create_oval(75, 200, 400, 450, fill="red", outline="")
elif output == "Blue":
    canvas.create_oval(200, 200, 525, 450, fill="blue", outline="")
elif output == "Green":
    canvas.create_oval(275, 100, 325, 230, fill="green", outline="")

root.mainloop()
