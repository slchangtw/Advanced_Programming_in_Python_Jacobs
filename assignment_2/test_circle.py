#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# JTSK-350112
# test_circle.py
# Shun-Lung Chang
# sh.chang@jacobs-university.de

from circle import Circle

if __name__ == '__main__':
    # initialize two circles
    c1 = Circle(3, 'white')
    c2 = Circle()
    
    # print information
    print(c1)
    print(c2)
    
    # add 
    print(c1 + c2)
    
    # subtraction
    print(c1 - c2)
    
    
    
