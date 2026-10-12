class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}  #n:i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in seen:
                return [seen[diff], i]
            seen[n] = i
        return [] 



# -3 1 2 4 7 9
#  i 
#            j