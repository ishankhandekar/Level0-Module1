"""
* Write a Python program that asks the user for two numbers.

* Then ask the user if the would like to add, subtract, multiply, or divide.

* Use if-else statements to provide the desired math operation on the numbers
  and display the result.
"""
from easygui import *
from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
  window = Tk()
  window.withdraw()
  num1 = simpledialog.askfloat("Simple Calculator","Enter a number")
  num2 = simpledialog.askfloat("Simple Calculator","Enter another number")
  
  choices = ["Multiplication","Division","Addition","Subtraction"]
  output = choicebox("What operation do you want to do?", "Simple Calculator", choices)
  
  if output == "Multiplication":
    messagebox.showinfo("Simple Calculator", str(num1) +" * " + str(num2) + " = " + str(num1 * num2))
  elif output == "Division":
    messagebox.showinfo("Simple Calculator", str(num1) +" / " + str(num2) + " = " + str(num1 / num2))
  elif output == "Addition":
    messagebox.showinfo("Simple Calculator", str(num1) +" + " + str(num2) + " = " + str(num1 + num2))
  elif output == "Subtraction":
    messagebox.showinfo("Simple Calculator", str(num1) +" - " + str(num2) + " = " + str(num1 - num2))
