#!/bin/python3

import math
import os
import random
import re
import sys

def divisibleSumPairs(n, k, ar):
    
    pairs = []
    pos_pairs = []

    for i in range(n):
        for j in range(n):
            if i != j:
                pos_pairs.append([ar[i],ar[j]])

    for i in pos_pairs:
        print(i[0],i[1])

    print("Length:",len(pos_pairs))

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
