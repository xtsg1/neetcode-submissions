# GREEN review 2026-11-16 | cold, alone, ~13 min, first try | O(n) time, O(1) space both right; dead l>=r guards from Nov 2 gone | tip: while l < r instead of while True | next review ~Dec 7
# rep nov 16

# QUESTION
# already sorted in ascending order- may have dupes
# indices of the 2 numbers that add to a target
# i1 and i2 are never equal
# return must have i1<i2
# always 1 solution
# only O(1) space
# return the INDICES not the numbers
# 1 indexed -_-

# APPROACH
# O(1) space means no set/dict allowed that grows with n
# pointers and single vars are the approach
# sorting buys us free O(nlogn)
# we can point from both ends
# check that they add to target
# dynamically increment/decrement based on if the sum is larger or smaller than target

# time: O(n) since both pointers just pass once
# space: O(1) bc only pointers and vars extra space


# solved in about 13m cold

class Solution:

    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l = 0
        r = len(numbers) - 1

        #always one solution
        while True: 

            s = numbers[l] + numbers[r]

            if s == target:
                return [l+1, r+1] #one-indexed....silly -_-
            
            if s <= target:
                l += 1
            elif s > target:
                r -= 1
            
        # dont have to worry about break because ALWAYS one solution
        





        