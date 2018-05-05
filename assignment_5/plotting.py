#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# JTSK-350112
# a5_6.py
# Shun-Lung Chang
# sh.chang@jacobs-university.de


import subprocess
import csv

if __name__ == '__main__':
    
    # make x (between -5 and 5) and x square 
    x = [i for i in range(-5, 6, 1)]
    x_square = [i ** 2 for i in x]
    
    # create square.dat
    with open('squares.dat', 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerows(zip(x, x_square))
    
    # plot
    proc = subprocess.Popen(['gnuplot'], shell = True, stdin = subprocess.PIPE)

    proc.stdin.write(b'set term png\n')
    proc.stdin.write(b'set output "result.png"\n')
    proc.stdin.write(b'plot "squares.dat" with linespoints\n')
    proc.stdin.write(b'quit\n')
    proc.stdin.flush()

    