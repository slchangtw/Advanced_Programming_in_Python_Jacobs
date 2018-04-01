#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 350112
# a6_2.py
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
    prob_dict = {"A": a, "B": b}
    return prob_dict, n

def gameOver(A, B):
    # A and B are scores for players in a racquetball game 
    # RETURNS true if game is over, false otherwise 
    
    return A == 15 or B == 15

def switch(serving):
    new_serving = ''
    
    if serving == "A":
        new_serving = "B"
    else: 
        new_serving = "A"
    
    return new_serving

def simOneGame(prob_dict):
    # Simulates a single game or racquetball between players A and B
    # RETURNS A's final score, B's final score
    
    serving = "A"
    score_dict = {"A": 0, "B": 0}
    
    while not gameOver(**score_dict):
        if random() < prob_dict[serving]:
            score_dict[serving] += 1
        else:
            serving = switch(serving)
            
    return score_dict

def simNGames(n, prob_dict):
    # Simulates n games of racquetball between players A and B 
    # RETURNS number of wins for A, number of wins for B
    
    wins_dict = {"A": 0, "B": 0}
    for i in range(n):
        score_dict = simOneGame(prob_dict) 
        
        largest_key = max(score_dict, key=score_dict.get)
        wins_dict[largest_key] += 1
    
    return wins_dict

def printSummary(A, B):
    # Prints a summary of wins for each player.
    
    n = A + B
    print("\nGames simulated: {0}".format(n))
    print("Wins for A: {0} ({1:0.1%})".format(A, A/n))
    print("Wins for B: {0} ({1:0.1%})".format(B, B/n))
    
def main():
    # main function
    
    printIntro()
    prob_dict, n = getInputs()
    wins_dict = simNGames(n, prob_dict)
    printSummary(**wins_dict)
    
if __name__ == "__main__":
    main()