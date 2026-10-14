# REDO

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        triplets = []
        
        for i in range(len(nums)):
            target = -nums[i]

            seen = set()
            for j in range(i+1, len(nums)):
                diff = target - nums[j]  # potential k's
                if diff in seen:
                    triplet = sorted([nums[i], nums[j], diff])  # [i,j,k]
                    if triplet not in triplets:
                        triplets.append(triplet)
                seen.add(nums[j])

        return triplets        




        



# 0 1 2 3 4 5 6
# i 
#   j

# i + j + k = 0
# j + k =  -i