#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# JTSK-350112
# game.py
# Shun-Lung Chang
# sh.chang@jacobs-university.de

from graphics import *
from craps import Player


def play_and_print():
    # initialize a player
    player = Player()
    
    # play a new game
    win_ = player.play()
    v1, v2 = player.getLastRoll()
    
    # texts (information about the roll)
    text = Text(Point(25, 25), "Dice 1: {0}".format(v1))
    text.draw(win)
    
    text = Text(Point(25, 45), "Dice 2: {0}".format(v2))
    text.draw(win)
    
    text = Text(Point(25, 65), "Sum: {0}".format(v1 + v2))
    text.draw(win)
    
    if win_:
        text = Text(Point(25, 85), "Won")
    else:
        text = Text(Point(25, 85), "Lost")
    text.draw(win)

    
if __name__ == '__main__':
    win = GraphWin()

    # field Play again
    field = Rectangle(Point(100, 25), Point(190, 55))
    field.draw(win)
    text = Text(Point(140, 40), "Play again")
    text.draw(win)

    # field Exit
    field = Rectangle(Point(100, 70), Point(190, 100))
    field.draw(win)
    text = Text(Point(140, 85), "Exit")
    text.draw(win)
    
    play_and_print()
    
    while True:
        # play a game
        p = win.getMouse()
        # if p is in field Play again
        if 100 < p.getX() < 190 and 25 < p.getY() < 55:
            # cover the text by a white rectangle
            shape = Rectangle(Point(5, 5), Point(80, 100))
            shape.setFill("white")
            shape.setOutline("white")
            shape.draw(win)
            
            play_and_print()
            
            continue
        # if p is in field Exit
        elif 100 < p.getX() < 190 and 70 < p.getY() < 100:
            win.close()
        else:
            shape = Rectangle(Point(0, 0), Point(80, 100))
            shape.setFill("white")
            shape.setOutline("white")
            shape.draw(win)
            
            