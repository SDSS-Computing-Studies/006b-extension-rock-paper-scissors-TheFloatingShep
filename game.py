#! python3

"""
Rock Paper Scissors Game!

Your documentation should go here
"""
# Import stuff
import tkinter as tk
import math
import random

# Stats
gP = 0
wins = 0
losses = 0
ties = 0
cR = 0
yR = 0
cP = 0
yP = 0
cS = 0
yS = 0

# When you start the game
def startGame():
  titleButton.pack_forget()
  tutorialButton.pack_forget()
  render()
  stats1.pack()
  stats2.pack()
  clearStats.pack()

# Opens tutorial
def openTutorial():
  tutorial.pack()
  titleScreen.pack_forget()
  tutorialCloseButton.pack()
  titleButton.pack_forget()
  tutorialButton.pack_forget()

# Close tutorial
def closeTutorial():
  titleScreen.pack()
  tutorial.pack_forget()
  tutorialCloseButton.pack_forget()
  titleButton.pack()
  tutorialButton.pack()

# Logic and stuff
def turn(x):
  global gP
  global wins
  global ties
  global losses
  global cR
  global cP
  global cS
# CPU pick
  y = math.ceil(random.randint(1,3))
  switcher = {
    1: "Rock",
    2: "Paper",
    3: "Scissors"
  }
# Display stuff
  rock.pack_forget()
  paper.pack_forget()
  scissors.pack_forget()
  titleScreen["text"] = "CPU: " + switcher.get(y)
  yourPick.pack()
  yourPick["text"] = "You: " + x
  continueButton.pack()
# Winner logic
  gP += 1
  if x == "Rock":
    if y == 1:
      z = "Tie"
      ties += 1
      cR += 1
    elif y == 2:
      z = "Lose"
      losses += 1
      cP += 1
    elif y == 3:
      z = "Win"
      wins += 1
      cS += 1
  elif x == "Paper":
    if y == 1:
      z = "Win"
      wins += 1
      cR += 1
    elif y == 2:
      z = "Tie"
      ties += 1
      cP += 1
    elif y == 3:
      z = "Lose"
      losses += 1
      cS += 1
  elif x == "Scissors":
    if y == 1:
      z = "Lose"
      losses += 1
      cR += 1
    elif y == 2:
      z = "Win"
      wins += 1
      cP += 1
    elif y == 3:
      z = "Tie"
      ties += 1
      cS += 1
# Show more stuff
  continueButton["text"] = z
  stats1["text"] = "|Games played: " + str(gP) + "|Wins: " + str(wins) + "|Losses: " + str(losses) + "|Ties: " + str(ties) + "|"
  stats2["text"] = "|Number of times picked: |Rock CPU: " + str(cR) + " YOU: " + str(yR) + "|Paper CPU: " + str(cP) + " YOU: " + str(yP) + "|Scissors CPU: " + str(cS) + " YOU: " + str(yS) + "|"

# Next turn
def nextTurn():
    render()
    continueButton.pack_forget()
    yourPick.pack_forget()

# Shows stuff
def render():
  rock.pack(side = tk.LEFT)
  paper.pack(side = tk.LEFT)
  scissors.pack(side = tk.LEFT)
  titleScreen["text"] = "Rock Paper Scissors!"

# Clears stats (no shame)
def clearStats():
  global gP
  global wins
  global ties
  global losses
  global cR
  global yR
  global cP
  global yP
  global cS
  global yS
  gP = 0
  wins = 0
  ties = 0
  losses = 0
  cR = 0
  yR = 0
  cP = 0
  yP = 0
  cS = 0
  yS = 0
  stats1["text"] = "|Games played: " + str(gP) + "|Wins: " + str(wins) + "|Losses: " + str(losses) + "|Ties: " + str(ties) + "|"
  stats2["text"] = "|Number of times picked: |Rock CPU: " + str(cR) + " YOU: " + str(yR) + "|Paper CPU: " + str(cP) + " YOU: " + str(yP) + "|Scissors CPU: " + str(cS) + " YOU: " + str(yS) + "|"

# When you pick a button
def rock():
  global yR
  yR += 1
  turn("Rock")
def paper():
  global yP
  yP += 1
  turn("Paper")
def scissors():
  global yS
  yS += 1
  turn("Scissors")

# All the widgets
main = tk.Tk()
main.geometry("500x200")
main.title("Rock Paper Scissors")
buttonsFrame = tk.Frame(pady = 20)
statsFrame = tk.Frame()
titleScreen = tk.Label(
  text="Welcome to Rock Paper Scissors",
  master = buttonsFrame
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
  command = rock,
  master = buttonsFrame
)
paper = tk.Button(
  text = "PAPER",
  command = paper,
  master = buttonsFrame
)
scissors = tk.Button(
  text = "SCISSORS",
  command = scissors,
  master = buttonsFrame
)
yourPick = tk.Label(
  text="",
  master = buttonsFrame
)
continueButton = tk.Button(
  text = "",
  command = nextTurn,
  master = buttonsFrame
)
stats1 = tk.Label(
  text = "|Games played: " + str(gP) + "|Wins: " + str(wins) + "|Losses: " + str(losses) + "|Ties: " + str(ties) + "|",
  master = statsFrame
)
stats2 = tk.Label(
  text = "|Number of times picked: |Rock CPU: " + str(cR) + " YOU: " + str(yR) + "|Paper CPU: " + str(cP) + " YOU: " + str(yP) + "|Scissors CPU: " + str(cS) + " YOU: " + str(yS) + "|",
  master = statsFrame
)
clearStats = tk.Button(
  text = "Clear stats",
  command = clearStats,
  master = statsFrame
)
# Pack everything
buttonsFrame.pack()
statsFrame.pack()
titleScreen.pack()
titleButton.pack()
tutorialButton.pack()

main.mainloop()

