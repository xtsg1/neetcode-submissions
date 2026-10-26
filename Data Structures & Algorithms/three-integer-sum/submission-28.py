
# Approach

# find the 3 numbers that sum to 0
# there must be negative numbers
# if x + y + z = 0 then that also means x + y = -z
# for each z we need to check if there two numbers that sum to -z

# so we're gonnna do the z loop we have to do O(n) at least
# we can use a seen dictionary that is O(n)
# so it will be O(n^2)

# secondary problem
# we require i, j, k to be distinct


# [-1,0,1,2,-1,-4]


class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        triplets = set()

        for i in range(len(nums)):

            z = nums[i]
            target = -z

            seen = set() 
            for j in range(i+1, len(nums)):
                
                complement = target - nums[j]
                if complement in seen:
                    x = complement
                    y = nums[j]
                    triplet = tuple(sorted((x,y,z))) #allows for dedupe
                    if triplet not in triplets:
                        triplets.add(triplet)

                seen.add(nums[j])

        triplets = [list(t) for t in triplets] 

        return triplets

                    
                

        