# rep november 24

# APPROACH
# ok so previously i used sum of series to find the missing number
# but why not use the range from n to len nums
# and nullify each against the number with a XOR
# XOR makes it so every bit cancels itself out 101 ^ 101 = 000
# whatever is leftover would be the missing number

# time: O(n) one for each number
# space: O(1) if we only use the range and no extra list


# walkthrough
# 1 2 3
# 0 1 2

class Solution:

    def missingNumber(self, nums: List[int]) -> int:

        x = 0 
        for i, n in enumerate(nums): 
            x = x ^ i ^ n
        
        last = len(nums)
        x = x ^ last

        return x




        
        




        