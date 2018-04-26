#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# JTSK-350112
# comp_students.py
# Shun-Lung Chang
# sh.chang@jacobs-university.de

from student import Student

if __name__ == '__main__':
    # create three students
    student_1 = Student('Alan', 1)
    student_2 = Student('Amy', 1)
    student_3 = Student('Alan', 1)
    
    # compare student 1 and student 2 
    print("Two different students:")
    print(student_1 == student_2)
    print(student_1 != student_2)
    print(student_1 < student_2)
    print(student_1 <= student_2)
    print(student_1 > student_2)
    print(student_1 >= student_2)
    
    # compare student 1 and student 3
    print("Two same students:")
    print(student_1 == student_3)
    print(student_1 != student_3)
    print(student_1 < student_3)
    print(student_1 <= student_3)
    print(student_1 > student_3)
    print(student_1 >= student_3)