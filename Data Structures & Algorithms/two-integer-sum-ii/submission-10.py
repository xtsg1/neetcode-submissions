# GREEN 2026-11-02 | cold, first try, 17:36 | two pointers O(n) / O(1); inner if l>=r / l<=r checks are dead code (always true/false inside while l<r)
# nov 2 cold rep

# QUESTION
# must be 2 indexed
# sum to target
# pre-sorted in ascending, may have dupes
# 2 numbers always unique
# always solution
# only O(1) space allowed

# APPROACH
# regular solve using a seen hashmap
# because pre-sorted we get free O(n*logn) already done for us
# so we can do one pass O(n)
# and use only pointers for memory O(1) and not a dict O(n)
# start with pointers at both ends l,r
# check if sum is equal to target
# if sum is too large move the larger of the two inwards
# if sum is too small move the smaller of the two inwards
# stop when pointers meet

# why 1-indexed? i dont get this part tho easy enough to do

# time: O(n)
# space: O(1)

# target = 6
# 1 1 1 2 4  
#       l r


#finished in 17:36

class Solution:

    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l = 0
        r = len(numbers) - 1

        while l < r:

            sm = numbers[l] + numbers[r] 

            if sm == target:
                i = l + 1
                j = r + 1
                return [i, j]

            elif sm > target:
                if l >= r:
                    l += 1
                else:
                    r -= 1

            elif sm < target:
                if l <= r:
                    l += 1
                else:
                    r -= 1
        
                
                     
        






