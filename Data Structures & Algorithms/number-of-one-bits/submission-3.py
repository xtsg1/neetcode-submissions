# GREEN 2026-11-21 | first sight, alone, first submit, 12:50 | add the complexity line: O(1) time (fixed 32 steps), O(1) space | review ~Nov 28
# first attempt nov 21

# QUESTION
# given a number - count the number of 1 bits
# n fits in 32 bits
# will be 1s and 0s

# APPROACH
# bit manipulation means using some operation to count 1s
# if we do n and 1, since 1 is actually ...0001
# the and & operator would 0 out everything, except the final value, in which case both have to be 1
# so in this way we can check if the 1st bit is a 1 or 0
# then all the bits can be bitshifted to the right 1 so that the 1 drops off the end
# shift it exactly 32 times i think


# solved: 12:50

class Solution:

    def hammingWeight(self, n: int) -> int:

        count = 0
        for _ in range(0, 32):

            
            is_one = n & 1
            if is_one == 1:
                count += 1
            n = n >> 1
        
        return count
            





        