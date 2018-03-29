#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 350112
# main_2.py
# Shun-Lung Chang
# sh.chang@jacobs-university.de

import sys
from mod_conversion import in2cm


start = int(input())
end = int(input())
step = int(input())
output = str(input())

(inches, cms) = in2cm(start, end, step)

start_str = '<html>\n<table>\n<tr> <th>inch</th><th>cm</th> </tr>\n'
table_str = ''
end_str = '</table>\n</html>'

for i in range(len(inches)):
    table_str += '<tr> <td>{0}</td><td>{1}</td> </tr>\n'.format(inches[i], cms[i])

result = start_str + table_str + end_str

if output == 's':
    html_file = open("in2cm.html", "w")
    html_file.write(result)
    html_file.close()
else:
    print(result)
    