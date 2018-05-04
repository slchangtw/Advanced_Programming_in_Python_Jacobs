#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# JTSK-350112
# a5_2.py
# Shun-Lung Chang
# sh.chang@jacobs-university.de

from graphics import *
import random

def pi_estimator(size, n_points):
    '''estimate and visualize pi'''
    
    # check validity of arguments 
    if size <= 0 or size > 1000:
        raise ValueError('Invalid size, size should be between 1 and 1000')
    if n_points <= 0:
        raise ValueError('Invalid n_points. n_points should be larger than 0')
    
    win = GraphWin("PI estimator", size, size)
    
    # count the number of points in the circle
    n_inside = 0
    
    for i in range(10000):
        x = random.uniform(0, size)
        y = random.uniform(0, size)
        
        if (x - (size / 2)) ** 2 + (y - (size / 2)) ** 2 <= (size ** 2) / 4:
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
    

if __name__ == '__main__':
    # estimate
    try:
        # inputs
        size = int(input('Enter the size of the window (between 1 and 1000):'))
        n_points = int(input('Enter the number of points (larger than 0):'))
            
        pi_estimator(size, n_points)
    except ValueError as e:
        print(e)