#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 350112
# a3_4.py
# Shun-Lung Chang
# sh.chang@jacobs-university.de

from cards import Deck

if __name__ == '__main__':
    deck = Deck()

    deck.shuffle()
    
    player_wins = 0
    dealer_wins = 0

    # the number of wins
    wins = 1    

    while(len(deck) > 0):

        player = deck.deal()
        dealer = deck.deal()

        if player == dealer:
            wins += 1 # added by 1
        elif player > dealer:
            player_wins += wins
            wins = 1 # reset the number of wins
        else:
            dealer_wins += wins
            wins = 1
        
    print("Player wins: {0}\nDealer wins: {1}".format(player_wins, dealer_wins))