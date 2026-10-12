class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        nums = sorted(nums)
        print(nums)

        i = 0
        longest = 0
        while i < len(nums):
            j = i + 1
            length = 1
            while j < len(nums) and nums[j] == (nums[i] + length):  #while consecutive
                j += 1
                length += 1
            if length > longest:
                longest = length
            i = j
            length = 1
    
        return longest

# 1 2 3 4 5 8 9 
# i           
#           j           


        