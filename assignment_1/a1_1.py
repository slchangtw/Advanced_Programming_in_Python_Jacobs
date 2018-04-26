#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# JTSK-350112
# a1_1.py
# Shun-Lung Chang
# sh.chang@jacobs-university.de

# inputs
start = int(input())
end = int(input())
step = int(input())

# create inches according to start, end and step
inches = list(range(start, end + step, step))
inches = [float(inch) for inch in inches]

# convert inch to cm 
cms = [inch * 2.54 for inch in inches]

# print results
print('{0:>5}{1:>10}'.format('inch', 'cm'))
for i in range(len(inches)):
    print('{0:5.1f}{1:>10.1f}'.format(inches[i], cms[i]))
