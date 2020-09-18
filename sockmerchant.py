#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    ar = sorted(ar)
    print(ar)
    pairs = 0
    i = 0
    while i < len(ar)-1:
        print(ar[i],ar[i+1])
        if ar[i] == ar[i+1]:
            pairs += 1
        i += 2
    return pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
