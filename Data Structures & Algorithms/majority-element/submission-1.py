#first attempt


# QUESTION
# more than half the time is majority element
# for sure exists
# arrays can be odd tho
# return majority element n


# APPROACH
# use a count dictionary
# select the highest count element
# early stop if any count > n/2 
# single loop so O(n) time
# using a finite dict so O(1)


# completed in 5:20

import math

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        majority_criterion = math.floor(len(nums) / 2)

        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1
            if counts.get(n) > majority_criterion:  #early stoppage
                return n
        

        