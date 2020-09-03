#!/usr/bin/python3
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4]

def nums(n):
    result = []
    s = 0
    for item in n:
        s += item
        result.append(s)
    return result