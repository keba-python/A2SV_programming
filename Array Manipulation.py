#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def arrayManipulation(n, queries):
    sum_arr = [0]* (n+2)
    max_val = 0
    
    for i in queries:
        a, b, c = i
        sum_arr[a] += c 
        sum_arr[b+1] -= c 
        
    for i in range(1,len(sum_arr)):
        sum_arr[i] += sum_arr[i-1]
        
        max_val = max(max_val, sum_arr[i])
  
    return max_val 
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
