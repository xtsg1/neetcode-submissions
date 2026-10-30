# oct 30 rep

# QUESTION
# consecutive run
# can have duplicates
# Must be O(n) which means no sorting
# numbers can be negative


# APPROACH
# use a hashset O(n)
# start with an item in nums
# check if n+1 exists
  #increment length
  #max length
     
# track the longest run thus far
# return the lenght of longest run
# one loop for checking is also O(n)

#STEPTHROUGH
#[2,20,4,10,3,4,5]
# 2

class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:  #quickstop
            return 0

        uniques = set(nums)
        longest = 1
        for n in nums:

            if (n-1) in uniques:
                pass

            if (n-1) not in uniques:
                length = 1
                while (n + 1) in uniques:
                    length += 1
                    n += 1
                longest = max(longest, length)
        
        return longest
            


                

        