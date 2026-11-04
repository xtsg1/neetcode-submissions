# rep nov 4

# QUE
# product of everything except nums[i]
# must be O(n), each element accessed once
# no division operator

# APPROACH
# two things have to be kept track of
# the cumulative products of everything left of pointer, and right of
# can it be done in one loop or multiple?
# we can precompute left and right cumulative products

# O(n) for time and space it should be

# Walkthrough
# 1 2 4 6

#lps = 1 2 8 24
#rps = 6 24 48 48


#solved in 20:35

class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # do left products first
        lps = [nums[0]]
        for i in range(1, len(nums)):
            lps.append(nums[i] * lps[i-1])
        
        # then right products
        rnums = nums[::-1]
        rps = [rnums[0]]
        for i in range(1, len(rnums)):
            rps.append(rnums[i] * rps[i-1])
        rps = rps[::-1] #reverse back


        # now do products
        products = []
        for i in range(len(nums)):
            if i == 0:
                lp = 1
                rp = rps[i+1]
            elif i == len(nums) - 1:
                rp = 1
                lp = lps[i-1]
            else:
                lp = lps[i-1]
                rp = rps[i+1]
            
            product = lp * rp
            products.append(product)
        
        return products
        

            
            


        