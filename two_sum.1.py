# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add 
# up to target.You may assume that each input would have 
# exactly one solution, and you may not use the same 
# element twice. You can return the answer in any order.

def two_sum(nums, target):
    di = dict()
    s = []
    for i in nums:
        di[i] = target - i
    for i in di.keys():
        if i in nums and di[i] in nums:
            if i == di[i] and nums.count(i) == 1:
                continue
            if i != di[i] :
                s.append(nums.index(i))
                s.append(nums.index(di[i]))
            else:
                s.append(nums.index(i))
                s.append(nums.index(i, nums.index(i) + 1))
            return s    

ls = [3, 2, 4, 11]
print(two_sum(ls, 6))
