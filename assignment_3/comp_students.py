#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 350112
# a3_1.py
# Shun-Lung Chang
# sh.chang@jacobs-university.de

from student import Student

if __name__ == '__main__':
    student_1 = Student('Alan', 1)
    student_2 = Student('Amy', 1)
    
    print(student_1 == student_2)
    print(student_1 != student_2)
    print(student_1 < student_2)
    print(student_1 <= student_2)
    print(student_1 > student_2)
    print(student_1 >= student_2)