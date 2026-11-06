# nov 6 rep

# QUESTION
# consecutive sequence
# each additional number can only be 1 greater
# can only be O(n) so no sorting

# APPROACH
# we can set nums
# check n+1 is in set
# track the longest length
# return longest

# walkthrough
# 2 20 4 10 3 4 5

class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:

        nset = set(nums)
        longest = 0
        
        for n in nums:
            length = 1 
            if n - 1 not in nset:
                start = n
                while (start+1) in nset:
                    length += 1
                    start += 1

                longest = max(longest, length) 
        
        return longest

        
        