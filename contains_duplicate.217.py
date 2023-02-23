# Given an integer array nums, return true if any value appears at least
# twice in the array, and return false if every element is distinct.

def cont_duplicate(nums):
    return len(nums) != len(set(nums))

ls = [1, 2, 3, 4, 5, 6]
ls1 = [1, 2, 3, 4, 5, 3, 6]
print(cont_duplicate(ls))
print(cont_duplicate(ls1))