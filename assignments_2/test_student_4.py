#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 350112
# a2_4.py
# Shun-Lung Chang
# sh.chang@jacobs-university.de

from student_4 import Student

if __name__ == '__main__':
    new_student = Student('John', 3)
    
    new_student.setScore(1, 100)
    new_student.setScore(2, 95)
    new_student.setScore(3, 50)
    
    print(new_student)
    
    new_student.setName('Jack')
    
    print(new_student)
