#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# JTSK-350112
# a5_4.py
# Shun-Lung Chang
# sh.chang@jacobs-university.de

import datetime

if __name__ == '__main__':
    
    # compute days that have passed
    last_eclipse = datetime.date(2017, 8, 21)
    today = datetime.date.today()
    delta = (today - last_eclipse).days
    
    print("It has been {0} days since last total solar eclipse.".format(delta))
    
