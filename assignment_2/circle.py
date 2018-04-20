#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# JTSK-350112
# student.py
# Shun-Lung Chang
# sh.chang@jacobs-university.de

from math import pi

class Circle(object):
    """Represents a circle."""
    
    def __init__(self, radius=1, color='red'):
        """constructor"""
        self._radius = radius
        self._color = color
    
    def getRadius(self):
        """Returns the radius"""
        return self._radius
    
    def setRadius(self, radius):
        """Resets the radius"""
        self._radius = radius
    
    def getColor(self):
        """Returns the color"""
        return self._color
    
    def serColor(self):
        """Resets the color"""
        self._color = color
        
    def getArea(self):
        """Returns the area"""
        return pi * (self._radius ** 2)
    
    def getPerimeter(self):
        """Returns the area"""
        return 2 * pi * self._radius
    
    def __add__(self, other):
        """overload add"""
        return self.getArea() + other.getArea()
    
    def __sub__(self, other):
        """overload sub"""
        return self.getArea() - other.getArea()
    
    def __str__(self): 
        """Returns the string representation of the circle."""
        return "Radius: {0:.2f}\nColor: {1}\nArea: {2:.2f}\nPerimeter: {3:.2f}\n".format(self._radius, \
                                                            self._color, self.getArea(), self.getPerimeter())
