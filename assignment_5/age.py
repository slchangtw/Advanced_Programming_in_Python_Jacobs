#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# JTSK-350112
# a5_5.py
# Shun-Lung Chang
# sh.chang@jacobs-university.de

import datetime


def get_age(text):
    """compute age"""
    
    for fmt in ('%Y-%m-%d', '%d.%m.%Y'):
        try:
            birth = datetime.datetime.strptime(text, fmt)
        except ValueError:
            pass
        else:
            today = datetime.date.today()
            return today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
    raise ValueError('Not a valid date or a date format. The format should be dd.mm.yyyy or yyyy-mm-dd')
    

if __name__ == '__main__':
    
    try:
        text = str(input('Please Enter your age in format dd.mm.yyyy or yyyy-mm-dd: '))
        age = get_age(text)
        
        if age < 0:
            print('Your age is negative. A wrong date was given')
        else:
            print('Your age is {0}'.format(age))
    except ValueError as e:
        print(e)
        
        