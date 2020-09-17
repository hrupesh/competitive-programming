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

    return 0


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
