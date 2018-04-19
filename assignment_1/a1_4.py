#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# JTSK-350112
# a1_4.py
# Shun-Lung Chang
# sh.chang@jacobs-university.de

if __name__ == '__main__':
    
    # create items
    items = list([(233, 'AAA', 10, 2422.5, 'location A'),
                  (199, 'BB', 90, 0.52, 'location B'), 
                  (222, 'CC', 100, 0.99, 'location C'), 
                  (332, 'DDDD', 190, 1.2, 'location D'),
                  (12, 'EEEE', 62, 200.56, 'location D')])
    
    # print column names
    print('{0:<5s}\t{1:<10}\t{2:>10}\t{3:>10}\t{4:>10}'.format('id', 'name', 'quantity', 'price', 'location'))
    
    # print items
    for item in items:
        print('{0:>05d}\t{1:<10}\t{2:>10}\t{3:>10,.2f}\t{4:>10}'.format(item[0], item[1], item[2], item[3], item[4]))
    