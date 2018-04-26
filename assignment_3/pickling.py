#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# JTSK-350112
# pickling.py
# Shun-Lung Chang
# sh.chang@jacobs-university.de

import sys
import pickle

from student import Student

if __name__ == '__main__':
    # create a student
    student_1 = Student('Amy', 1)
    
    print('The size of the object:', sys.getsizeof(student_1))
    
    # pickle the object
    with open('object.txt', 'wb') as f:
        pickle.dump(student_1, f, pickle.HIGHEST_PROTOCOL)
    
    