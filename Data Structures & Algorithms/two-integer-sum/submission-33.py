# REP: oct 20

class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        diffs = []

        for i, n in enumerate(nums):

            if n in diffs:
                output_i = diffs.index(n)
                output_j = i
                return [output_i, output_j]
            
            diff = target - n 
            diffs.append(diff)
        
        



#target = 8
# 1 3 4 5 6 7 2
#           i

# 7 5 4 3 2  