#! python3

"""
Rock Paper Scissors Game!

Your documentation should go here
"""

import os
import tkinter as tk

def main():
  def text1():
    titleScreen["text"] = "COOL BEANS"
    openTutorial()

  def openTutorial():
    tutorial.pack()
    titleScreen.label.pack_forget()
  def closeTutorial():
    tutorial.widget.pack_forget()

  main = tk.Tk()
  main.geometry("500x500")
  main.title("Rock Paper Scissors")
  titleScreen = tk.Label(
    text="Welcome to Rock Paper Scissors",
  )
  titleButton = tk.Button(
    text = "START",
    command=text1
  )
  tutorialButton = tk.Button(
    text = "TUTORIAL",
    command=openTutorial
  )
  tutorial = tk.Label(
    text="Do you really not know how to play rock paper scissors?"
  )

  titleScreen.pack()
  titleButton.pack()
  tutorialButton.pack()
  main.mainloop()


main()
