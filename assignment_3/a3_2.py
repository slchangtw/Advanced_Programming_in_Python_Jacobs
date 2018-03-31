#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 350112
# a3_2.py
# Shun-Lung Chang
# sh.chang@jacobs-university.de

from student import Student
import random

if __name__ == '__main__':
    student_1 = Student('Amy', 1)
    student_2 = Student('Emma', 1)
    student_3 = Student('Jimmy', 1)
    student_4 = Student('John', 1)
    student_5 = Student('Tom', 1)
    student_6 = Student('Jack', 1)
    student_7 = Student('Mike', 1)
    student_8 = Student('Olivia', 1)
    student_9 = Student('Sophia', 1)
    student_10 = Student('Susan', 1)
    
    # put students into a list
    student_list = [student_1, student_2, student_3, student_4, student_5,
                   student_6, student_7, student_8, student_9, student_10]
    
    # shuffle the list
    random.shuffle(student_list)
    
    # sort the list
    student_list.sort()
    
    # print the result
    for student in student_list:
        print(student)