# GREEN 2026-11-01 | cold, 5 min | one-pass hashmap, O(n) / O(n)
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
