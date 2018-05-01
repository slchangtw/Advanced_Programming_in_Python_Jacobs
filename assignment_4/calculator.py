#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# JTSK-350112
# calculator.py
# Shun-Lung Chang
# sh.chang@jacobs-university.de

from graphics import *

def layout():
    '''build the layout'''
    # instruction
    Text(Point(64, 10), "1. Enter two numbers").draw(win)
    Text(Point(70, 20), "2. Press one operations").draw(win)
    Text(Point(70, 180), "Click elsewhere to leave").draw(win)

    # interface
    Text(Point(50, 50), "First Number:").draw(win)
    Text(Point(50, 70), "Second Number:").draw(win)

    # result panel
    shape = Rectangle(Point(0, 130), Point(200, 170))
    shape.setFill('grey')
    shape.setOutline('grey')
    shape.draw(win)
    
    # operation buttons
    operators = ['+', '-', '*', '/']
    for i in range(4):
        shape = Rectangle(Point(10 + i * 30, 100), Point(30 + i * 30, 120))
        shape.setFill("pink")
        shape.draw(win)

        text = Text(Point(20 + i * 30, 110), "{0}".format(operators[i]))
        text.draw(win)

def compute(number_1, number_2, X_, Y_):
    '''compute result'''
    try:
        if 10 < X_ < 30 and 100 < Y_ < 120:
            return number_1 + number_2
        if 40 < X_ < 60 and 100 < Y_ < 120:
            return number_1 - number_2
        if 70 < X_ < 90 and 100 < Y_ < 120:
            return number_1 * number_2
        if 100 < X_ < 120 and 100 < Y_ < 120:
            return number_1 / number_2
        else:
            # leave if click elsewhere
            win.close()
    except ZeroDivisionError:
        return 'inf'
    except TypeError:
        return 'invalid value'
   
def refresh_screen(s):
    '''refresh result'''
    
    shape = Rectangle(Point(0, 130), Point(200, 170))
    shape.setFill('grey')
    shape.setOutline('grey')
    shape.draw(win)
    
    Text(Point(100, 150), '{0}'.format(s)).draw(win)

if __name__ == '__main__':
    # create layout
    win = GraphWin()
    layout()
    entry_1 = Entry(Point(150, 50), 4)
    entry_1.setText('0.0')
    entry_1.draw(win)

    entry_2 = Entry(Point(150, 70), 4)
    entry_2.setText("0.0")
    entry_2.draw(win)
    
    while True:
        p = win.getMouse()
        try:
            num_1 = eval(entry_1.getText())
            num_2 = eval(entry_2.getText())
            X_, Y_ = p.getX(), p.getY()
            s = compute(num_1, num_2, X_, Y_)
        except SyntaxError:
            s = 'invalid value'
        finally:
            refresh_screen(s)
            
  