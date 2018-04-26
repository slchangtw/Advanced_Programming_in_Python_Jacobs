#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# JTSK-350112
# raise_exc.py
# Shun-Lung Chang
# sh.chang@jacobs-university.de


def something():    
    try:
        input_ = int(input("Please enter an integer:"))
        if input_ == 1:
            raise ValueError("999")
        elif input_ == 2:
            raise ValueError("Error has happend")
        elif input_ == 3:
            raise ValueError("1.23")
        else:
            print("The integer is: {0}".format(input_))
    except ValueError as v:
        print(v)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise
    finally:
        print("Good bye")

if __name__ == '__main__':
    # do something
    something()
    
