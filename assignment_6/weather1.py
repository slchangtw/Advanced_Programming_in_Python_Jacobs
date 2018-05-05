#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# JTSK-350112
# a6_4.py
# Shun-Lung Chang
# sh.chang@jacobs-university.de


import urllib.request
from urllib.error import URLError, HTTPError

if __name__ == '__main__':
    try:
        month = int(input("Enter a month (between 1 and 12): "))
        # padding 0 
        month = str(month).zfill(2)
        url = 'https://grader.eecs.jacobs-university.de/courses/350112/python/csv/exp2008' + month + '.csv'
        
        file = urllib.request.urlopen(url).read()

        with open('wdata1.csv', 'wb') as f: 
            f.write(file)
    
    except ValueError as e:
        print(e)
    except (HTTPError, URLError):
        print("Error fetching URL: ", url)  
    
