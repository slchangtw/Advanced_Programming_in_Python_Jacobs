#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# JTSK-350112
# a5_3.py
# Shun-Lung Chang
# sh.chang@jacobs-university.de

from graphics import *

if __name__ == '__main__':
    
    win = GraphWin("PI estimator", 255, 255)
    
    # print points
    for i in range(255):
        for j in range(255):
            color = color_rgb(0 + i * 1, 0 + j * 1, 0)
            if (i + j) % 150 == 0:
                win.plotPixel(i, j, color)
            else:
                win.plotPixelFast(i, j, color)
                
    win.getMouse()
    win.close()
