# GREEN 2026-11-20 | alone, first submit, untimed (first bit session) | the iso == 0 OR branch is redundant: res ^= n alone works | review ~Nov 27
# first attempt nov 5

# QUESTION
# only one number is not duplicated
# find it
# each element can only be accessed once O(n)
# only O(1) space so no list/dicts etc... hmm

# APROACH
# the trick is apparently bit manipulation
# so what are the properties here?
# would converting everything to bits do anything for us? 
#
# ok so if 3=100, and 2 is 010 what i noticed is if i try the ^ operator one after the other whats leftover is 010 which is 2
# now im not sure how the logic of this works exactly is a bit fuzzy but maybe it can extend let me try a few other numbers
# somehow the two 3s cancel out
# let me try 4 8 4 2 2
# 0100 ^ 1000 ^ 0100 ^ 0010 ^ 0010 = 1000 = 8 wow
# WOW it works, somehow XOR cancels itself out, its like a pure bitwise negation or something (still a bit fuzz)
# so it seemsl ike the whole trick is to XOR it all??
# how to init? what is the behaviour of XOR on none? 0? 
# oh maybe we can init 0 and use a regular OR

class Solution:

    def singleNumber(self, nums: List[int]) -> int:

        iso = 0

        for n in nums:
            # ok so apparently you can just use bitwise operators on integers directly

            if iso == 0:
                iso = iso | n  #just assign n
            else:
                iso = iso ^ n  #cancels out itself
        
        return iso








        