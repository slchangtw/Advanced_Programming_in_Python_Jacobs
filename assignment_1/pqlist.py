#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# JTSK-350112
# pqlist.py
# Shun-Lung Chang
# sh.chang@jacobs-university.de

from bisect import bisect

def is_empty(pq):
    """
    return true if pq is empty
    """
    
    return not pq


def insert_with_priority(pq, x, p):
    """
    insert new element with priority
    """
    
    # find the index where the new element should be inserted
    ind = bisect([elem[1] for elem in pq], p)
    pq.insert(ind,(x, p))
    
def pull_highest_priority_element(pq):
    """
    pull element with the highest priority
    """
    
    # find the index where the element with the highest priority
    ind, _ = min(enumerate(pq), key=lambda k: k[1][1])
    print(pq[ind][0])
    pq.pop(ind)
    
if __name__ == '__main__':
    # initialize pq
    pq = []
    
    # insert elements
    insert_with_priority(pq, 5, 2)
    print(pq)
    insert_with_priority(pq, 3, 3)
    print(pq)
    insert_with_priority(pq, 13, 1)
    print(pq)
    insert_with_priority(pq, 6, 1)
    print(pq)
    
    # pull the element with the highest priority
    pull_highest_priority_element(pq)
    
    # check if pq is empty
    print(is_empty(pq))
    