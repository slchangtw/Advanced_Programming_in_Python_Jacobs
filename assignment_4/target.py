#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# JTSK-350112
# target.py
# Shun-Lung Chang
# sh.chang@jacobs-university.de

from graphics import *

def draw_archery(*circles):
    # unpack circles
    circles = circles[0]
    
    colors = ('white', 'black', 'blue', 'red', 'yellow')
    
    win = GraphWin()
    win.setBackground('pink')
    
    for i in range(len(circles)):
        circle = Circle(Point(circles[i][0], circles[i][1]), circles[i][2])
        circle.setFill(colors[i])
        circle.draw(win)
    
    message = Text(Point(80, 195), "Click anywhere to quit")
    message.draw(win)
    win.getMouse()

if __name__ == '__main__':
    # draw target
    draw_archery([(100, 100, 75), (100, 100, 60), (100, 100, 45), (100, 100, 30), (100, 100, 15)])
    
