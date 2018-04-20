#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# JTSK-350112
# test_craps.py
# Shun-Lung Chang
# sh.chang@jacobs-university.de

from craps import playOneGame
from craps import playManyGames

if __name__ == '__main__':
    # play five games
    for i in range(5):
        playOneGame()
    
    # play many games
    playManyGames()
