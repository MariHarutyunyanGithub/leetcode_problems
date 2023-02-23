# Given an integer array nums, find the subarray 
# with the largest sum, and return its sum.

import sys

def max_sub(nums):
    max_sum = -sys.maxsize
    current_max = 0
    for i in nums:
        current_max += i
        max_sum = max(max_sum, current_max)
        current_max = max(current_max, 0)
    return max_sum 

ls = [5, -4, -1, 2, 3, -6, 7, 8, 9, -6, ]
print(max_sub(ls))