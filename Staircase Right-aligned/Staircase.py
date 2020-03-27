#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.

'''Multiple arguments to print() adds a space:'''
def staircase(n):
    space = n-2
    for stair in range(1,n):
        print(' '*space,'#'*stair)
        space = space - 1
    print('#'*n)
    '''
    for i in range(n):
        flag = 0
        for j in range(n,-1,-1):
            if(i == j or flag == 1):
                print('#',end='')
                flag = 1
            else:
                print(' ',end='')
        print('\n')
    '''   
if __name__ == '__main__':
    n = int(input())

    staircase(n)
