#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# JTSK-350112
# draw_face.py
# Shun-Lung Chang
# sh.chang@jacobs-university.de

from graphics import *

if __name__ == '__main__':
    win = GraphWin()
    
    # draw a face
    face = Circle(Point(100, 100), 90)
    face.draw(win)
    
    left_eye = Circle(Point(70, 70), 20)
    left_eye.setFill("red")
    left_eye.draw(win)
    
    right_eye = Circle(Point(130, 70), 20)
    right_eye.setFill("red")
    right_eye.draw(win)
    
    nose = Polygon(Point(80, 100), Point(120, 100), Point(100, 120))
    nose.setFill("cyan")
    nose.draw(win)
    
    upper_lip = Rectangle(Point(70, 140), Point(130, 145))
    upper_lip.setFill("pink")
    upper_lip.draw(win)
    
    lower_lip = Rectangle(Point(70, 145), Point(130, 150))
    lower_lip.setFill("pink")
    lower_lip.draw(win)
    
    left_ear = Rectangle(Point(5, 100), Point(10, 110))
    left_ear.setFill("blue")
    left_ear.draw(win)
    
    right_ear = Rectangle(Point(190, 100), Point(195, 110))
    right_ear.setFill("blue")
    right_ear.draw(win)
    
    message = Text(Point(80, 195), "Click anywhere to quit")
    message.draw(win)
    win.getMouse()
    
    