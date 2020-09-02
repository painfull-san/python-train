#!/usr/bin/python3

def fib(n):
  fib1 = 0
  fib2 = 1
  a = []
  while len(a) < n:
    fib1, fib2 = fib2, fib1 + fib2
    if fib1 % 2 == 0:
        a.append(fib1)
  print(a)

fib(10)

# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4]
