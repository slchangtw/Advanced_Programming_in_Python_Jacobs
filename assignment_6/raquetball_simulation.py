#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 350112
# a6_1.py
# Shun-Lung Chang
# sh.chang@jacobs-university.de

from random import random

def printIntro():
    # Prints an introduction to the program
    
    print("This program simulates a game of racquetball between two") 
    print('players called "A" and "B". The abilities of each player is') 
    print("indicated by a probability (a number between 0 and 1) that") 
    print("the player wins the point when serving. Player A always") 
    print("has the first serve.\n")
    
def getInputs():
    # RETURNS probA, probB, number of games to simulate
    
    a = float(input("What is the prob. player A wins a serve? "))
    b = float(input("What is the prob. player B wins a serve? "))
    n = int(input("How many games to simulate? "))
    return a, b, n

def gameOver(a,b):
    # a and b are scores for players in a racquetball game 
    # RETURNS true if game is over, false otherwise 
    
    return a == 15 or b == 15

def simOneGame(probA, probB):
    # Simulates a single game or racquetball between players A and B
    # RETURNS A's final score, B's final score
    
    serving = "A"
    scoreA = 0
    scoreB = 0
    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else:
                serving = "B"
        else:
            if random() < probB:
                scoreB = scoreB + 1
            else:
                serving = "A"
    return scoreA, scoreB

def simNGames(n, probA, probB):
    # Simulates n games of racquetball between players A and B 
    # RETURNS number of wins for A, number of wins for B
    
    winsA = 0
    winsB = 0
    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB) 
        if scoreA > scoreB:
            winsA = winsA + 1
        else:
            winsB = winsB + 1
    return winsA, winsB

def printSummary(winsA, winsB):
    # Prints a summary of wins for each player.
    
    n = winsA + winsB
    print("\nGames simulated: {0}".format(n))
    print("Wins for A: {0} ({1:0.1%})".format(winsA, winsA/n))
    print("Wins for B: {0} ({1:0.1%})".format(winsB, winsB/n))
    
def main():
    # main function
    
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(n, probA, probB)
    printSummary(winsA, winsB)
    
if __name__ == "__main__":
    main()