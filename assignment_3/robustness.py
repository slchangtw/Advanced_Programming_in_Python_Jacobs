#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# JTSK-350112
# robustness.py
# Shun-Lung Chang
# sh.chang@jacobs-university.de


def example1():
    try:
        for i in range(3):
            x = int(input("enter a number: "))
            y = int(input("enter another number: "))
            print(x, '/', y, '=', x/y)
    except ZeroDivisionError:
        print('y cannot be zero')
    except ValueError as e:
        print(e)

def example2(L):
    try:
        print("\n\nExample 2")
        sum = 0
        sumOfPairs = []
        for i in range(len(L)):
            sumOfPairs.append(L[i]+L[i+1])

        print("sumOfPairs = ", sumOfPairs)
    except IndexError as e:
        print(e)
    except TypeError as e:
        print(e)


def printUpperFile(fileName):
    try:
        file = open(fileName, "r")
        for line in file:
            print(line.upper())
        file.close()
    except FileNotFoundError as e:
        print(e)
    
def main():
    
    try:
        example1()
        L = [10, 3, 5, 6, 9, 3]
        example2(L)
        example2([10, 3, 5, 6, "NA", 3])
        example3([10, 3, 5, 6 ])

        printUpperFile("doesNotExistYest.txt")
        printUpperFile("./Dessssktop/misspelled.txt")
    except NameError as e:
        print(e)

main()
