#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# JTSK-350112
# main.py
# Shun-Lung Chang
# sh.chang@jacobs-university.de

from mod_conversion import in2cm_table

if __name__ == '__main__':

    # inputs
    start = int(input())
    end = int(input())
    step = int(input())
    output = str(input())
    
    # covert inches to cms
    (inches, cms) = in2cm_table(start, end, step)

    # html strings
    start_str = '<html>\n<table>\n<tr> <th>inch</th><th>cm</th> </tr>\n'
    table_str = ''
    end_str = '</table>\n</html>'
    
    # create a html table
    for i in range(len(inches)):
        table_str += '<tr> <td>{0}</td><td>{1}</td> </tr>\n'.format(inches[i], cms[i])

    result = start_str + table_str + end_str

    if output == 's':
        html_file = open("in2cm.html", "w")
        html_file.write(result)
        html_file.close()
    else:
        print(result)
    