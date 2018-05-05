#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# JTSK-350112
# a6_3.py
# Shun-Lung Chang
# sh.chang@jacobs-university.de

from random import random

def get_inputs():
    # RETURNS prob_a, prob_b, number of games to simulate
    
    a = float(input("What is the prob. player A wins a serve (between 0 and 1)? "))
    b = float(input("What is the prob. player B wins a serve (between 0 and 1)? "))
    n = int(input("How many games to simulate (larger than 0)? "))
    
    if not (0 <= a <= 1) or not (0 <= b <= 1) or n <= 0:
        raise ValueError('Some inputs are invalid.')
    return a, b, n

def game_over(a, b, sanctioned=False):
    # a and b are scores for teams in a volleyball game 
    # RETURNS true if game is over, false otherwise 
    
    if not sanctioned:
        return (a >= 15 or b >= 15) and (abs(a-b) >= 2)
    else:
        return a == 25 or b == 25

def sim_one_game(prob_a, prob_b, sanctioned=False):
    # Simulates a single game between teams A and B
    # RETURNS A's final score, B's final score
    
    serving = "A"
    score_a = 0
    score_b = 0
    
    while not game_over(score_a, score_b, sanctioned): 
        if serving == "A":
            if random() < prob_a:
                score_a = score_a + 1
            else:
                if sanctioned:
                    score_b = score_b + 1
                serving = "B"
        else:
            if random() < prob_b:
                score_b = score_b + 1
            else:
                if sanctioned:
                    score_a = score_a + 1
                serving = "A"
            
    return score_a, score_b
    

def sim_n_games(n, prob_a, prob_b, sanctioned=False):
    # Simulates n games between teams A and B 
    # RETURNS number of wins for A, number of wins for B
    
    wins_a = 0
    wins_b = 0
    
    for i in range(n):
        score_a, score_b = sim_one_game(prob_a, prob_b, sanctioned) 
        if score_a > score_b:
            wins_a = wins_a + 1
        else:
            wins_b = wins_b + 1

    return wins_a, wins_b 

def print_summary(wins_a, wins_b):
    # Prints a summary of wins for each player.
    
    n = wins_a + wins_b
    print("\nGames simulated: {0}".format(n))
    print("Wins for A: {0} ({1:0.1%})".format(wins_a, wins_a/n))
    print("Wins for B: {0} ({1:0.1%})".format(wins_b, wins_b/n))
    
def main():
    # main function

    prob_a, prob_b, n = get_inputs()
    
    wins_a, wins_b = sim_n_games(n, prob_a, prob_b, sanctioned=False)
    print_summary(wins_a, wins_b)
    
    wins_a, wins_b = sim_n_games(n, prob_a, prob_b, sanctioned=True)
    print_summary(wins_a, wins_b)
    
if __name__ == '__main__':
    try:
        main()
    except ValueError as e:
        print(e)
    
"""If player A has a higher probability winning a serve, he/she will
    win more games in first kind of volleyball game. On the contrary,
    if player B has a higher probability, he/she will win more games in 
    second kind of volleyball game."""