# first attempt

# QUESTION
# nums has 0, 1, 2 ... n
# find the missing number in nums
# time must be O(n)
# space must be O(1)
# array unsorted

# APPROACH
# why cant i just do a loop from 0 to n and check whether n in set(nums)
# because that would be O(n) space hmm
# why cant we do n and check if n+1 in nums, because its still requires a set or time complexity goes over
# omg is this that math trick
# sum of sequence S = n/2(a1 + an)
# so we just add up all the nums and compare against this
# the diff is the missing number ._.


class Solution:

    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)

        expected = n * (n+1)/2
        actual = sum(nums)

        diff = int(abs(expected - actual))
        return diff
        