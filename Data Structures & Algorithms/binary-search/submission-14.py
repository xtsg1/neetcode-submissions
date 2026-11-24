# GREEN 2026-11-24 | cold, no hints, 13 min, O(log n) time O(1) space | review ~Dec 1
# rep nov 24

#APPROACH
# for O(logn) we need to implement binary search
# start with two pointers at edged
# cut in half and floor
# check if target is ><= to midpoint
# higher target, move left pointer past midpoint
# vice versa lower target
# end conditions are:
    # pointers never crossover
    # midpoint equivalent to target
    # not equivalent return -1

# time: O(logn) for binary search
# space: 3 pointers so O(1)

# WALKTHROUGH
#target = 4
#        
# -1 0 2 4 6 8
#          m
#        l          
#            r 

# solved: 13:18 with two errors self fix
# had direction of logic wrong had m = (l - r)
# had the wrong symbol, the midpoint is the sum floor divided not the difference

class Solution:

    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums) - 1

        while l <= r:

            m = (r + l) // 2  #floor divide

            if nums[m] == target:
                return m
            elif nums[m] <= target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
        
        return -1 #not found

                

        