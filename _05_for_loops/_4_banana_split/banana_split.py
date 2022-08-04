"""
* 1. Look at the image bananasplit.png

* 2. Your mission is to create a python program that recreates that image
     using the create_text function
     
* 3. The catch is, you can only type the create_text function ONE TIME ONLY
     into your program. Using a loop and if-statements, you must figure out
     how to vary the text and the positioning so that you can read all four
     separate lines.
"""

from tkinter import *
import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width=200, height=200, bg="#FF00FF")
canvas.grid()

'''
Text Rendering Example:
                    x    y                                                       
canvas.create_text(100, 50, text="text goes here", font=("Arial", 16))
'''
text1 = ""
x = 0
y = 0
# Put your code below
for i in range(4):
     if i == 0:
          text1 = "ice cream"
          x = 100
          y = 50
     elif i == 1:
          text1 = "ice cream"
          x = 100
          y = 30
     elif i == 2:
          text1 = "ice cream"
          x = 100
          y = 10
     elif i == 3:
          text1 = "banana"
          x = 100
          y = 70
     canvas.create_text(x, y, text = text1, font=("Arial", 16))
     
          
          

root.mainloop()
