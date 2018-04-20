#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# JTSK-350112
# student.py
# Shun-Lung Chang
# sh.chang@jacobs-university.de

class Student(object):
    """Represents a student."""
    
    def __init__(self, name, number):
        """All scores are initially 0."""
        self._name = name
        self._scores = []
        
        for i in range(number):
            self._scores.append(0)
        print('Constructor being called')

    def getName(self):
        """Returns the student's name."""
        return self._name

    def setScore(self, i, score):
        """Resets the ith score, counting from 1."""
        self._scores[i - 1] = score

    def getScore(self, i):
        """Returns the ith score, counting from 1."""
        return self._scores[i - 1]

    def getAverage(self):
        """Returns the average score."""
        return sum(self._scores) / len(self._scores)

    def getHighScore(self):
        """Returns the highest score."""
        return max(self._scores)

    def __str__(self):
        """Returns the string representation of the student."""
        return "Name: " + self._name  + "\nScores: " + \
                " ".join(map(str, self._scores))
        

if __name__ == '__main__':
    # initilize three students
    student_1 = Student('Jenny', 2)
    student_2 = Student('Steve', 2)
    student_3 = Student('Celine', 2)
     
    # set scores
    student_1.setScore(1, 95)
    student_1.setScore(2, 90)
    
    student_2.setScore(1, 95)
    student_2.setScore(2, 90)
    
    student_3.setScore(1, 95)
    student_3.setScore(2, 90)
    
    # print the results
    print(student_1)
    print(student_2)
    print(student_3)
