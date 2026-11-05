# rep nov 5

# Question
# a duplicate exists
# distinct indices
# distance between indices less than k? is this arbitrary?

# Approach
# make a seen hashmap of n:i
# check for duplicate if its been seen
# check if the duplicate is lesser distance than k
# return t/f

# time: O(n) loop through elements once
# space: O(n) needs a seen hashmap to be created

# stepthrough

# k=3
# 1 0 1 1
#     i

# 1: 0
# 0: 1


# i messed myself up a bit by using continue ending the loop early
# still solved in 12:10 though


class Solution:

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        seen = {}

        for i, n in enumerate(nums):

            if n in seen:
                j = seen[n]
                if abs(i - j) <= k:
                    return True
            
            seen[n] = i
        
        return False

        