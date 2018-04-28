#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# JTSK-350112
# raise_exc.py
# Shun-Lung Chang
# sh.chang@jacobs-university.de

# self-defined exceptions
class OneOwnError(Exception): 
    pass
    
class TwoOwnError(Exception): 
    pass

class ThreeOwnError(Exception): 
    pass

def something():    
    try:
        input_ = int(input("Please enter an integer:"))
        
        if input_ == 1: 
            raise OneOwnError
        elif input_ == 2: 
            raise TwoOwnError
        elif input_ == 3: 
            raise ThreeOwnError
    
    except OneOwnError as e:
        print("Exception with {0} has been raised".format(999))
    except TwoOwnError as e:
        print("Exception with {0} has been raised".format("Error has happend"))
    except ThreeOwnError as e:
        print("Exception with {0} has been raised".format("1.23"))
    except:
        print("An unexpected error occurred")
        raise
    else:
        print("The integer is: {0}".format(input_))
    finally:
        print("Nice try!")

if __name__ == '__main__':
    # do something five times
    print("Enter five different integers.")
    for i in range(5):
        something()
    
