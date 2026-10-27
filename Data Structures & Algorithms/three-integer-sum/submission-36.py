
# Approach

# return all triplets
# no duplicate triplets

# first create a target
# x + y + z = 0
# x + y = -z
# find x + y that equals -z
# outer loop for each number in z O(n)
# inner loop, instead of using seen set/hashmap
# use two pointers from both ends
# only works on a sorted list O(n*logn)
# time complexity is still O(n^2)
# space complexity O(n) one list

class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # first step is sort to get asc property
        nums.sort()

        triplets = set()
        for i in range(len(nums) - 2):  # O(n)
            z = nums[i]
            l = i + 1
            r = len(nums) - 1 

            # [-1, 0, 1]
            while l < r:
                
                x = nums[l]
                y = nums[r]

                if (x + y) == -z:  # x + y + z = 0
                    triplet = tuple(sorted([x, y, z]))
                    triplets.add(triplet)
                    l += 1
                elif (x + y) < -z: 
                    l += 1
                elif (x + y) > -z:
                    r -= 1

        output = []
        for t in triplets:
            output.append(list(t))
        
        return output


                        



        





        