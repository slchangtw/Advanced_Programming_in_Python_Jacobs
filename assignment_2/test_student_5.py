#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# JTSK-350112
# test_student.py
# Shun-Lung Chang
# sh.chang@jacobs-university.de

from student_5 import Student

if __name__ == '__main__':
    # initialize a new student
    new_student = Student('John', 2, 20)
    
    # set scores
    new_student.setScore(1, 100)
    new_student.setScore(2, 90)
    
    print(new_student)
    
    # set new age
    new_student.setAge(21)
    
    print(new_student)
    