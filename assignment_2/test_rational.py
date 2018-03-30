#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 350112
# test_rational.py
# Shun-Lung Chang
# sh.chang@jacobs-university.de

from rational import Rational

if __name__ == '__main__':
    first = Rational(1, 2)
    second = Rational(1, 8)
    
    sum_ = first + second
    
    print(sum_)
    