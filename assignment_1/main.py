#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 350112
# main.py
# Shun-Lung Chang
# sh.chang@jacobs-university.de

import sys
from mod_conversion import in2cm_table


start = int(input())
end = int(input())
step = int(input())
print_option = str(input())

in2cm_table(start, end, step)
