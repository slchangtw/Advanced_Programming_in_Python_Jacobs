#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 350112
# a1_1.py
# Shun-Lung Chang
# sh.chang@jacobs-university.de

import sys


start = int(input())
end = int(input())
step = int(input())

inches = list(range(start, end + step, step))
inches = [float(inch) for inch in inches]

cms = [inch * 2.54 for inch in inches]

print('{0}{1:>10}'.format('inch', 'cm'))
for i in range(len(inches)):
    print('{0:.1f}{1:>10.1f}'.format(inches[i], cms[i]))
