#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    ac = 0
    oc = 0
    for dist in apples:
        if dist > 0 :   #towards right
            if a + dist >= s and a + dist <= t:
                ac += 1
    for dist in oranges:
        if dist < 0 :   #towards left
            if b + dist >= s and b + dist <= t:
                oc += 1   
    print(ac)         
    print(oc)


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
