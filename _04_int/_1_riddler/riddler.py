"""
* Write a python program that asks the user a minimum of 3 riddles.

* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got
  correct
"""
import turtle
from tkinter import messagebox, simpledialog, Tk
import math
if __name__ == '__main__':
  score = 0
  window=Tk()
  window.withdraw()
  
  answer1 = simpledialog.askstring("Riddler","The more you take, the more you leave behind. What am I?")
  if answer1.lower() == "footsteps": 
    messagebox.showinfo("Correct!")
    score += 1
  else:
    messagebox.showinfo("Incorrect, the correct answer was footsteps")
    score -= 1
  
  answer1 = simpledialog.askstring("Riddler","What has six faces, but does not wear makeup, has twenty-one eyes, but cannot see? What is it?")
  if answer1.lower() == "dice": 
    messagebox.showinfo("Correct!")
    score += 1
  else:
    messagebox.showinfo("Incorrect, the correct answer was a dice")
    score -= 1
  
  answer1 = simpledialog.askstring("Riddler","I am not alive, but I grow; I don't have lungs, but I need air; I don't have a mouth, but water kills me. What am I?")
  if answer1.lower() == "fire": 
    messagebox.showinfo("Correct!")
    score += 1
  else:
    messagebox.showinfo("Incorrect, the correct answer was fire")
    score -= 1
    
  messagebox.showinfo("Your score was " + score)
  
  