#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 350112
# mod_conversion.py
# Shun-Lung Chang
# sh.chang@jacobs-university.de


def in2cm_table(start, end, step):
    """convert inch to cm"""
    """print results"""
    
    inches = list(range(start, end + step, step))
    inches = [float(inch) for inch in inches]

    cms = [inch * 2.54 for inch in inches]

    print('{0}{1:>10}'.format('inch', 'cm'))
    for i in range(len(inches)):
        print('{0:.1f}{1:>10.1f}'.format(inches[i], cms[i]))
        
def in2cm(start, end, step):
    """convert inch to cm"""
    """return results"""
    
    inches = list(range(start, end + step, step))
    inches = [float(inch) for inch in inches]

    cms = [inch * 2.54 for inch in inches]
    
    return (inches, cms)
