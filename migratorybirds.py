#!/bin/python3

import math
import os
import random
import re
import sys


def migratoryBirds(arr):
    b1 = 0
    b2 = 0
    b3 = 0
    b4 = 0
    b5 = 0

    for i in arr:
        if i == 1:
            b1 += 1
        elif i == 2:
            b2 += 1
        elif i == 3:
            b3 += 1
        elif i == 4:
            b4 += 1
        else:
            b5 += 1

    s = [b1, b2, b3, b4, b5]
    print(s)

    max = s[0]
    max_index = 0
    for i in range(len(s)):
        if s[i] > max:
            max = s[i]
            max_index = i

    print(max_index, max)
    if max_index == 0:
        return 1
    elif max_index == 1:
        return 2
    elif max_index == 2:
        return 3
    elif max_index == 3:
        return 4
    elif max_index == 4:
        return 5
    else:
        return 0


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
