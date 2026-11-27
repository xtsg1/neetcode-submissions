# SEEN 2026-11-27 | after solution video | cold solve ~Nov 29
# first attempt untimed



class Solution:

    def climbStairs(self, n: int) -> int:
        one = 1
        two = 1

        for i in range(n - 1):

            temp = one
            one = one + two
            two = temp
        
        return one

