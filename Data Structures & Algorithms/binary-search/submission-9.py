# first attempt nov 20

# QUESTION
# sorted ascending
# find target
# if index DNE return -1
# basically run a binary search

# APPROACH
# use a left and right pointer
# find a midpoint
# check if midpoint is smaller or larger than target
# larger: shift l to midpoint + 1 (midpoint was wrong)
# smaller: shift r to midpoint - 1
# invariant? l and r pointers should never crossover so l < r
# but l and be r land on the same number, midpoint would be that number, if not found loop would end
# end of loop return -1
# return the INDEX or -1


# walkthrough
# target = 4
# -1 0 2 4 6 8
#        l
#        r
#          m

class Solution:

    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums) - 1

        while l <= r:

            m = (l + r) // 2  #floor division

            if nums[m] == target:  #m is always the checker, even when l==r m will run one last time
                return m
            elif nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
        
        return -1
            

        