#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 350112
# a4_1.py
# Shun-Lung Chang
# sh.chang@jacobs-university.de

from graphics import *

if __name__ == '__main__':
    win = GraphWin()
    
    # draw a square with length of 30
    shape = Rectangle(Point(20, 20), Point(50, 50))
    shape.setOutline("blue")
    shape.setFill("blue")
    shape.draw(win)
    
    # draw another 10 squares
    for i in range(10):
        p = win.getMouse()
        shape = Rectangle(Point(p.getX(), p.getY()), Point(p.getX()+30, p.getY()+30))
        shape.setOutline("blue")
        shape.setFill("blue")
        shape.draw(win)
    
    win.close()
    
