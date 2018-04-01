#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 350112
# a4_4.py
# Shun-Lung Chang
# sh.chang@jacobs-university.de

from graphics import *

if __name__ == '__main__':
    win = GraphWin()
    
    p1 = win.getMouse()
    p2 = win.getMouse()
    
    rect = Rectangle(Point(p1.getX(), p1.getY()), Point(p2.getX(), p2.getY()))
    rect.setFill("red")
    rect.draw(win)
    
    message = Text(Point(80, 195), "Click anywhere to quit")
    message.draw(win)
    win.getMouse()
    
    
