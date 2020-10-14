#! python3

"""
Rock Paper Scissors Game!

Your documentation should go here
"""
import tkinter as tk

def main():
  def startGame():
    titleScreen["text"] = "Rock Paper Scissors!"
    titleButton.pack_forget()
    tutorialButton.pack_forget()
    turn()

  def openTutorial():
    tutorial.pack()
    titleScreen.pack_forget()
    tutorialCloseButton.pack()
    titleButton.pack_forget()
    tutorialButton.pack_forget()

  def closeTutorial():
    titleScreen.pack()
    tutorial.pack_forget()
    tutorialCloseButton.pack_forget()
    titleButton.pack()
    tutorialButton.pack()

  def turn():
    rock.pack()
    paper.pack()
    scissors.pack()

  def rock():
    pass
  def paper():
    pass
  def scissors():
    pass

  main = tk.Tk()
  main.geometry("500x500")
  main.title("Rock Paper Scissors")
  titleScreen = tk.Label(
    text="Welcome to Rock Paper Scissors"
  )
  titleButton = tk.Button(
    text = "START",
    command = startGame
  )
  tutorialButton = tk.Button(
    text = "TUTORIAL",
    command = openTutorial
  )
  tutorial = tk.Label(
    text = "Do you really not know how to play rock paper scissors?"
  )
  tutorialCloseButton = tk.Button(
    text = "CLOSE",
    command = closeTutorial
  )
  rock = tk.Button(
    text = "ROCK",
    command = rock
  )
  paper = tk.Button(
    text = "PAPER",
    command = paper
  )
  scissors = tk.Button(
    text = "SCISSORS",
    command = scissors
  )
  

  titleScreen.pack()
  titleButton.pack()
  tutorialButton.pack()
  main.mainloop()

main()
