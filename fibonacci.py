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