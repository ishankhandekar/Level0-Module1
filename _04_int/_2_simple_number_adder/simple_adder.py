from tkinter import messagebox, simpledialog, Tk
"""
* Write a Python program that asks the user for two numbers.

* Display the sum of the two numbers to the user
"""
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    num1 = simpledialog.askfloat("Simple Adder","Enter a number to add")
    num2 = simpledialog.askfloat("Simple adder","Enter another number")
    messagebox.showinfo("Simple Adder",str(num1) + " + " + str(num2) + " = " + str(num1 + num2))