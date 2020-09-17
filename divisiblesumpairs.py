#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.


def divisibleSumPairs(n, k, ar):
    
    pairs = []
    pos_pairs = []

    for i in range(n):
        for j in range(n):
            if i < n -1 and i != j:
                pos_pairs.append([ar[i],ar[j]])

    print(pos_pairs)

    for i in pos_pairs:
        print(i)

    return 0


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
