# rep nov 25

# APPROACH
# unsorted so cannot two pointer
# for each one store in a seen dictionary
# check each one for if the complement has been seen
# if the complement has been seen then the match is found
# return first index then second index

# time: O(n)
# space: O(n) for dict

#solved 6:04
class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}
        for i, n in enumerate(nums):

            diff = target - n

            if diff in seen:
                i1 = seen[diff]
                i2 = i
                return [i1, i2]

            seen[n] = i
    
            



                


        