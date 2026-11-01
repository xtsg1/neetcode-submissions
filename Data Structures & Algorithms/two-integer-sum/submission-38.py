# rep nov 1

class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {} # n:i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in seen:
                i1 = seen[diff]
                i2 = i
                return [i1, i2]
            seen[n] = i
