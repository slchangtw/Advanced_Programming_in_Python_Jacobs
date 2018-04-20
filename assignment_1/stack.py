#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# JTSK-350112
# stack.py
# Shun-Lung Chang
# sh.chang@jacobs-university.de


def push(stack, element):
    stack.append(element)
    print('Pushing {0}'.format(element))
def pop(stack):
    if len(stack) == 0:
        print('Stack underflow')
    else:
        print('Popping element {0}'.format(stack.pop()))
def empty(stack):
    print('Popping element {0}'.format(stack.pop(0)))
    del stack[:]
    
    
if  __name__ == '__main__':
    stack = []
    while True:
        command = str(input())
        if command == 'q':
            print('Good Bye!')
            break
        if command == 's':
            element = int(input())
            push(stack, element)
        if command == 'p':
            pop(stack)
        if command == 'e':
            empty(stack)
            
