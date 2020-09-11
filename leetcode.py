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

#Sort the matrix diagonally
def diagonalSort(mat):
        m, n = len(mat), len(mat[0])

        for i in range(m):
            j_range = range(min(m - i, n))
            diag_mat = sorted(mat[i + j][j] for j in j_range)
            for j in j_range:
                mat[i + j][j] = diag_mat[j]

        for j in range(1, n):
            i_range = range(min(n - j, m))
            diag_mat = sorted(mat[i][i + j] for i in i_range)
            for i in i_range:
                mat[i][i + j] = diag_mat[i]

        return mat



#One number
#Given a non-empty array of integers, every element appears twice except for one. Find that single one.

def singleNumber(nums):
    a = []
    b = []
    nums.sort()
    for i in range(len(nums)):
        if i % 2 == 0:
            a.append(nums[i])
        else:
            b.append(nums[i])
    a = set(a)
    b = set(b)
    if len(b) > len(a):
        c = b - a
    else:
        c = a - b
    c = list(c)
    return c[0]

def singleNumber1(nums): #Здесь используется манипулирование битами. Самый эффективный вариант. Надо разобраться как работает
    a = 0
    for i in nums:
        a ^= i
    return a

singleNumber1([17,12,5,-6,12,4,17,-5,2,-3,2,4,5,16,-3,-4,15,15,-4,-5,-6])