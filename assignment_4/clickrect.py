#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# JTSK-350112
# clickrect.py
# Shun-Lung Chang
# sh.chang@jacobs-university.de

from graphics import *

if __name__ == '__main__':
    win = GraphWin()
    
    p1 = win.getMouse()
    p2 = win.getMouse()
    
    # get coordinates
    p1_X = p1.getX()
    p1_Y = p1.getY()
    p2_X = p2.getX()
    p2_Y = p2.getY()
    
    rect = Rectangle(Point(p1_X, p1_Y), Point(p2_X, p2_X))
    rect.setFill("red")
    rect.draw(win)
    
    message = Text(Point(80, 195), "Click anywhere to quit")
    message.draw(win)
    win.getMouse()
    
    # compute perimeter and area
    perimeter = abs(((p2_X - p1_X) + (p2_Y - p1_Y)) * 2)
    area = abs((p2_X - p1_X) * (p2_Y - p1_Y))
    
    print('Perimeter is {0}'.format(perimeter))
    print('Area is {0}'.format(area))
    
