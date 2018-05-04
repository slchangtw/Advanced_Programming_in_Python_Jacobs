#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# JTSK-350112
# a5_6.py
# Shun-Lung Chang
# sh.chang@jacobs-university.de


import Gnuplot
import pickle

if __name__ == '__main__':
    
    # make x (between -5 and 5) and x square 
    x = [i for i in range(-5, 6, 1)]
    x_square = [i ** 2 for i in x]
    
    # put x and x square into a dictionary
    dic_x = {'x': x, 'x_square': x_square}
    
    # print x and x square
    for i in range(len(dic_x['x'])):
        print('x is {0} and x square is {1}'.format(dic_x['x'][i], dic_x['x_square'][i]))
        
    # make square.dat
    with open('square.dat', 'wb') as f:
        pickle.dump(dic_x, f, pickle.HIGHEST_PROTOCOL)
    
    # plot
    g = Gnuplot.Gnuplot()
    d = Gnuplot.Data(dic_x['x'], dic_x['x_square'], with_="lines")
    g.plot(d)
    
    # save the plot
    g.hardcopy(filename='result.png', terminal = 'png') 
    
    