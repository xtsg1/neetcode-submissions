# rep oct 30

# Approach
# use a set
# gets unique nums
# the set should be the same length as the array

# time complexity should be O(1)
# space complexity should be O(n) 

# 1 2 3 3
# 1 2 3
# 

class Solution:

    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = set(nums)
        if len(unique) < len(nums):
            return True
        return False
        
        

        