#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# JTSK-350112
# test_complex.py
# Shun-Lung Chang
# sh.chang@jacobs-university.de

from complex import Complex

if __name__ == '__main__':
    # create two complex numbers
    u = Complex(1, 2)
    v = Complex(2, 3)
    
    # test operators
    print(u + v)
    print(u - v)
    print(u * v)
    print(u / v)