#!/bin/python3

import math
import os
import random
import re
import sys


def birthday(s, d, m):

    ways = 0

    for i in range(len(s)):
        if i > 0:
            if s[i-1] + s[i] == d:
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
