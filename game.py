#! python3

"""
Rock Paper Scissors Game!

Your documentation should go here
"""
import tkinter as tk
import math
import random

def main():
  def startGame():
    titleButton.pack_forget()
    tutorialButton.pack_forget()
    render()

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

  def turn(x):
    y = math.ceil(random.randint(1,3))
    switcher = {
      1: "Rock",
      2: "Paper",
      3: "Scissors"
    }
    rock.pack_forget()
    paper.pack_forget()
    scissors.pack_forget()
    titleScreen["text"] = "Computer: " + switcher.get(y)
    yourPick.pack()
    yourPick["text"] = "You: " + x
    continueButton.pack()
    if x == "rock":
      if y == 1:
        z = "Tie"
      elif y == 2:
        z = "Lose"
      elif y == 3:
        z = "Win"
    elif x == "paper":
      if y == 1:
        z = "Win"
      elif y == 2:
        z = "Tie"
      elif y == 3:
        z = "Lose"
    elif x == "scissors":
      if y == 1:
        z = "Lose"
      elif y == 2:
        z = "Win"
      elif y == 3:
        z = "Tie"
    continueButton["text"] = z

  def nextTurn():
    render()
    continueButton.pack_forget()
    yourPick.pack_forget()

  def render():
    rock.pack()
    paper.pack()
    scissors.pack()
    titleScreen["text"] = "Rock Paper Scissors!"

  def rock():
    turn("rock")
  def paper():
    turn("paper")
  def scissors():
    turn("scissors")

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
  yourPick = tk.Label(
    text=""
  )
  continueButton = tk.Button(
    text = "",
    command = nextTurn
  )
  stats = tk.Label(
    text = "|Games played: |Wins: |Losses: |Ties|"
  )

  titleScreen.pack()
  titleButton.pack()
  tutorialButton.pack()
  main.mainloop()

main()
