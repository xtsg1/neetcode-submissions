# GREEN 2026-11-23 | cold, no hints, 24 min | review ~Nov 30
# 1st attempt nov 23

# APPROACH
# how to reverse the binary representation
# if we do n & 1 then it will be 1 only if both are 1
# assign that to the ones column (end)
# start at the end then shuffle everything over 1 << 

# WALKTHROUGH

# n 10101
# &1 00001
# if 1: res 00000 | 00001 = 00001
# res <<  00010
# if not 1, just shift 0
# ahh i forgot to shift n over so im just repeating the same 1

# Solved: in 24 min with only 1 min to spare. shape of solution in maybe 10m but really had trouble with the loops

class Solution:

    def reverseBits(self, n: int) -> int:
        
        res = 0
        for _ in range(0, 32):  # i identified an off by 1 error and fixed it but a little fuzzy on exactly why?

            print(f"n{n:032b} res{res:032b}")
            res = res << 1  # a bit fuzzy on why this must happen first
            digit = n & 1
            if digit == 1:
                res = res | 1
            n = n >> 1

        
        return res
        


        