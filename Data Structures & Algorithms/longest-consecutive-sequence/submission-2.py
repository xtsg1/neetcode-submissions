class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:

        
        nums = sorted(list(set(nums)))
        print(nums)

        largest = 0
        for i in range(0, len(nums)):
            consecutive_n = 1
            j = i
            while j < len(nums) - 1 and (nums[j+1] - nums[j]) == 1:
                consecutive_n = consecutive_n + 1
                j = j + 1
            
            if consecutive_n > largest:
                largest = consecutive_n
        
        return largest

                


            

            


        