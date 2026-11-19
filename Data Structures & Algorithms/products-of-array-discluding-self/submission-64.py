# rep nov 19

# QUESTION
# each element in list
# product of everything else


# APPROACH
# What we need is a product of everything left of i
# then a product of everything right of i
# so two pointers really
# then for all of i grab everything left and right and multiply it together
# return the list

# STEPS
# 1 2 4 6

# L 1   2   8    48
# R 48  48  24   6

# Solved in 23 minutes, some hicucps but worked through without external help

class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:

        lps = [[] for _ in range(len(nums))]
        rps = [[] for _ in range(len(nums))]

        for i in range(len(nums)):
            j = len(nums) - 1 - i

            lp = nums[i] * lps[i-1] if i else nums[i]
            rp = nums[j] * rps[j+1] if j < (len(nums) - 1) else nums[j]

            lps[i] = lp
            rps[j] = rp
        
        res = []
        for i in range(len(nums)):
            left = lps[i-1] if i else 1
            right = rps[i+1] if i < (len(nums) - 1) else 1
            p = left * right
            res.append(p)
        
        return res
        

        








        