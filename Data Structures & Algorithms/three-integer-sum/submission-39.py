# rep nov 8

# QUESTION
# 3 distinct nums add to 0
# return i,j,k
# all triplets, not just one
# order doesn't matter
# list of lists output

# APPROACH
# we use x + y + z = 0
# therefore x + y = -z
# so we can set -z as target
# then check for x and y that add to target (seen map)
# for valid i,j,k we need to dedupe them
# set of sorted tuples

# time: 2 for loops therfore O(n^2)
# space: O(n) only one growing dict/list to track

# solved in 14:30

# WALKTHROUGH

# -1 0 1 2 -1 -4
#  i   j

# z = -1
# target = 1

# seen 0
# diff 0

# x = 0
# y = 1

# triplet (-1, 0, 1)



class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        triplets = set()

        for i in range(len(nums)):
            z = nums[i]
            target = -z

            seen = set()
            for j in range(i+1,len(nums)):
                
                diff = target - nums[j]
                if diff in seen:
                    x = diff
                    y = nums[j]
                    triplet = tuple(sorted([x,y,z]))
                    triplets.add(triplet)
                
                seen.add(nums[j])

        res = [] 
        for t in triplets:
            res.append(list(t))
        
        return res

                
                    


        