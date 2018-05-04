#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# JTSK-350112
# a5_1.py
# Shun-Lung Chang
# sh.chang@jacobs-university.de

from graphics import *
import random

if __name__ == '__main__':
    d = 400
    win = GraphWin("PI estimator", d, d)
    
    # count the number of points in the circle
    n_inside = 0
    
    for i in range(10000):
        x = random.uniform(0, d)
        y = random.uniform(0, d)
        
        if (x - (d / 2)) ** 2 + (y - (d / 2)) ** 2 <= (d ** 2) / 4:
            # if i is divisible by 1000, use plotPixel()
            if i % 1000 == 0:
                win.plotPixel(x, y, 'red')
            else:
                win.plotPixelFast(x, y, 'red')
            n_inside += 1
        else:
            if i % 1000 == 0:
                win.plotPixel(x, y, 'blue')
            else:
                win.plotPixelFast(x, y, 'blue')
                
        # print estimated pi on the screen every 100 iterations 
        if i % 100 == 0 and i != 0:
            ratio = n_inside / i * 4
            print(ratio)
    
    win.getMouse()
    win.close()