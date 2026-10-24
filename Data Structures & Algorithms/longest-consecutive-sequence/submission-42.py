class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        
        longest = 0
        for n in nums:
            if (n - 1) not in numset:
                consecutive = 1
                while (n + consecutive) in numset:
                    consecutive += 1
                longest = max(longest, consecutive)
        
        return longest
            



                

            


# {2, 3, 4, 5, 10, 20}