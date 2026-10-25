# O(1) attempt

# Approach
# use two pointers L and R
# check if L + R is equal to target
# if its too high, move the larger number inward
# if its too low move the smaller number inward

# target: 6
# 1 2 4 8 9
#   i j
# there will always be one solution
# edge case is duplicates
# 1 2 2 2 4 8 9
# L and R should never be equivalent unless they meet in the middle and thats exactly where the solution is


class Solution:


    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        L = 0
        R = len(numbers) - 1

        while L < R:

            nsum = numbers[L] + numbers[R]

            if nsum == target:
                i = L + 1
                j = R + 1
                return [i, j]

            if nsum > target:
                R -= 1
            
            if nsum < target:
                L += 1


        