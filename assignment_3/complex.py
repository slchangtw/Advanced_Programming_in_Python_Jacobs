#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 350112
# a3_5.py
# Shun-Lung Chang
# sh.chang@jacobs-university.de

class Complex(object):
    
    def __init__(self, real, imag):
        self._real = real
        self._imag = imag
        
    def __add__(self, other):
        if type(self) != type(other):
            raise raiseTypeError('Type of {0} is not same as Type of {1}'.format(type(self), type(other)))
        
        return Complex(self._real + other._real, self._imag + other._imag)
    
    def __sub__(self, other):
        if type(self) != type(other):
            raise raiseTypeError('Type of {0} is not same as Type of {1}'.format(type(self), type(other)))
            
        return Complex(self._real - other._real, self._imag - other._imag)
    
    def __mul__(self, other):
        if type(self) != type(other):
            raise raiseTypeError('Type of {0} is not same as Type of {1}'.format(type(self), type(other)))
            
        return Complex(self._real * other._real - self._imag * other._imag,
                       self._real * other._imag + other._real * other._real)
    
    def __truediv__(self, other):
        if type(self) != type(other):
            raise raiseTypeError('Type of {0} is not same as Type of {1}'.format(type(self), type(other)))
         
        return Complex((self._real * other._real + self._imag * other._imag) / (other._real ** 2 +  other._imag ** 2), (self._imag * other._real - self._real * other._imag) /  (other._real ** 2 +  other._imag ** 2))
    
    def __str__(self):
        return "Real Part: {0:.2f}\nImaginary Part: {1:.2f}".format(self._real, self._imag)
        
        