#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# JTSK-350112
# a6_5.py
# Shun-Lung Chang
# sh.chang@jacobs-university.de


import urllib.request
from urllib.error import URLError, HTTPError
import csv
from datetime import datetime


if __name__ == '__main__':
    try:
        url = 'https://grader.eecs.jacobs-university.de/courses/350112/python/csv/exp200803.csv'
        response = urllib.request.urlopen(url)
    except (HTTPError, URLError):
        print("Error fetching URL: ", url)
    
    # retrive data 
    files = response.readlines()
    files = [file.decode('utf-8').split(',') for file in files] 
     
    # write data into a csv file
    with open('wdata2.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['date', 'time', 'temperature', 'humid', 'wind', 'direction'])
        for item in files[3:]:
            try:
                date = datetime.strptime(item[0], '%d.%m.%Y')
                if date.day == 11:
                    date = date.strftime('%y-%m-%d')
                    time = item[1]
                    temperature = item[2]
                    humid = item[3]
                    wind = item[6]
                    direction = item[7]
                    writer.writerow([date, time, temperature, humid, wind, direction])
            except:
                pass
            
