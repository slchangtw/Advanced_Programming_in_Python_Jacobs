#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 350112
# mod_conversion.py
# Shun-Lung Chang
# sh.chang@jacobs-university.de


def in2cm_table(start, end, step):
    """convert inch to cm"""
    """and print results"""
    
    # 
    inches = list(range(start, end + step, step))
    inches = [float(inch) for inch in inches]

    cms = [inch * 2.54 for inch in inches]
    
    return (inches, cms)
