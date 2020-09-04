#!/usr/bin/python3
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4]
#Runnung sum of 1d array
def nums(n):
    result = []
    s = 0
    for item in n:
        s += item
        result.append(s)
    return result

#Shuffle the array
def shuffle(nums, n):
    a = nums[:n]
    b = nums[n:]
    c = []
    for i, j in zip(a,b):
        c.append(i)
        c.append(j)
    return c

#Valid Palindrome 
#Работает, но не очень эффективно
#Runtime: 116 ms, faster than 5.44% of Python3 online submissions for Valid Palindrome.
#Memory Usage: 14.8 MB, less than 37.76% of Python3 online submissions for Valid Palindrome.
def isPalindrome(s):
        delChar = list("\\'!@#$%^&*(){}[]_+:\\ \"|\?/><,.;*-`~")
        a = s.lower()
        a = ''.join(list(filter(lambda c: c not in delChar, a)))
        if a == a[::-1]:
            return True
        else:
            return False