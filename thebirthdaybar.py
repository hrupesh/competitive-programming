#!/bin/python3

import math
import os
import random
import re
import sys

def birthday(s, d, m):
    
    ways = 0

    t = []

    for i in range(len(s)):
        temp = 0
        for j in range(m):
            if i + j < len(s):
                temp += s[i+j]
        t.append(temp)
    print(t)

    for i in t:
        if i == d:
            ways += 1
    
    return ways


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
