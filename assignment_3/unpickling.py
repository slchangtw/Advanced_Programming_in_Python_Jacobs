#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# JTSK-350112
# unpickling.py
# Shun-Lung Chang
# sh.chang@jacobs-university.de

import sys
import pickle

from student import Student

if __name__ == '__main__':
    # open 'object.txt'
    with open('object.txt', 'rb') as f:
        student_1 = pickle.load(f)
        
    print(student_1)
    
    sum_ = 0
    with open('object.txt', 'rb') as f:
        content = f.readlines()
        print(content)
        sum_ += sys.getsizeof(content)
        
    print('Sum of the size:', sum_)
        
    