#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 350112
# main.py
# Shun-Lung Chang
# sh.chang@jacobs-university.de

from mod_conversion import in2cm_table

# inputs
start = int(input())
end = int(input())
step = int(input())

# convert inches to cms, and return results
inches, cms = in2cm_table(start, end, step)

# print results
print('{0:>5}{1:>10}'.format('inch', 'cm'))
for i in range(len(inches)):
    print('{0:5.1f}{1:>10.1f}'.format(inches[i], cms[i]))
