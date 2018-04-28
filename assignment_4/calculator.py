#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# JTSK-350112
# calculator.py
# Shun-Lung Chang
# sh.chang@jacobs-university.de

from graphics import *

class calculator(object):
    """define a calculator"""
    
    def __init__(self):
        self._layout()
        self._first_num = ''
        self._second_num = ''
        self._operator = ''
    
    def _layout(self):

        # print numbers
        numbers = [7, 8, 9, 4, 5, 6, 1, 2, 3]
        for i in range(3):
            for j in range(3):
                shape = Rectangle(Point(20 + j * 40, 40 + i * 40), Point(50 + j * 40, 70 + i * 40))
                shape.setFill("pink")
                shape.draw(win)

                text = Text(Point(35 + j * 40, 55 + i * 40), "{0}".format(numbers[j + i + 2 * i]))
                text.draw(win)

        # 0
        shape = Rectangle(Point(20, 160), Point(50, 190))
        shape.setFill("pink")
        shape.draw(win)

        text = Text(Point(35, 175), "0")
        text.draw(win)

        # print operators 
        operators = ['+', '-', '*', '/', '=']
        for i in range(5):
            shape = Rectangle(Point(150, 40 + i * 30), Point(190, 60 + i * 30))
            shape.setFill("pink")
            shape.draw(win)

            text = Text(Point(170, 50 + i * 30), "{0}".format(operators[i]))
            text.draw(win)

        # .
        shape = Rectangle(Point(100, 170), Point(120, 180))
        shape.setFill("pink")
        shape.draw(win)

        text = Text(Point(110, 175), ".")
        text.draw(win)

    def click(self, X_coord, Y_coord):
        s = ''
        if 20 < X_coord < 50 and 40 < Y_coord < 70:
            s = '7'
        if 60 < X_coord < 90 and 40 < Y_coord < 70:
            s = '8'
        if 100 < X_coord < 130 and 40 < Y_coord < 70:
            s = '9'
        if 20 < X_coord < 50 and 80 < Y_coord < 110:
            s = '4' 
        if 60 < X_coord < 90 and 80 < Y_coord < 110:
            s = '5' 
        if 100 < X_coord < 130 and 80 < Y_coord < 110:
            s = '6' 
        if 20 < X_coord < 50 and 120 < Y_coord < 150:
            s = '1'
        if 60 < X_coord < 90 and 120 < Y_coord < 150:
            s = '2'
        if 100 < X_coord < 130 and 120 < Y_coord < 150:
            s = '3'
        if 20 < X_coord < 50 and 160 < Y_coord < 190:
            s = '0'
        if 150 < X_coord < 190 and 40 < Y_coord < 60:
            self._operator = '+'
        if 150 < X_coord < 190 and 70 < Y_coord < 90:
            self._operator = '-'
        if 150 < X_coord < 190 and 100 < Y_coord < 120:
            self._operator = '*'
        if 150 < X_coord < 190 and 130 < Y_coord < 150:
            self._operator = '/'
        if 100 < X_coord < 120 and 170 < Y_coord < 180:
            s = '.'
        # equal sign
        if 150 < X_coord < 190 and 160 < Y_coord < 180:
            s = str(self._compute())
        
        # set first_num to inf if first_num is 'inf'
        if self._first_num == 'inf':
            self._first_num = ''
            
        if self._first_num == '' or self._operator == '':
            self._first_num += s
        else:
            self._second_num += s
            
        self._refresh_screen(self._first_num + self._operator + self._second_num)    

    def _refresh_screen(self,string):
        shape = Rectangle(Point(10, 10), Point(180, 30))
        shape.setFill("white")
        shape.setOutline("white")
        shape.draw(win)

        text = Text(Point(100, 20), "{0}".format(string))
        text.draw(win)
        
    def _compute(self):
        num1 = float(self._first_num)
        num2 = float(self._second_num)
        
        if self._operator == '+':
            result = num1 + num2
        if self._operator == '-':
            result =  num1 - num2
        if self._operator == '*':
            result = num1 * num2
        if self._operator == '/':
            if num2 == 0: 
                result = 'inf'
            else:
                result = num1 / num2
        
        self._first_num = ''
        self._second_num = ''
        self._operator = ''
        
        return result
        
if __name__ == '__main__':
    win = GraphWin()
    c = calculator()
    while True:
        p = win.getMouse()
        X_, Y_ = p.getX(), p.getY()
        c.click(X_, Y_)
    win.close()
    
    