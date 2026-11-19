# rep nov 19

# QUESTION
# distinct i and j
# where duplicated
# AND the absolute value of i-j is less than k
# in other words they are not further than k apart

# APPROACH
# the abs(i-j) sounds to me like a sliding window algorithm of size k
# initiate a sliding window of size k
# check whether duplicate exists within that sliding window of k
# if it exists we return True EARLY
# only once the window slid to the end and nothing found then we can return False
# window size is static k
# whole window can slide as one no need to dynamically append/pop from window
# use a set to keep track of unique elements within the k window
# the size of set can never be over k

# time: whole window slides across once so O(n)
# space: worst case window is as large as n so O(n)


# k = 3
# 1 2 3 1 7 8 9 8
# 0    
#       3  # but slicing is exclusive

class Solution:

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:


        l = 0
        r = l + k

        uniques = [] 
        for i in range(len(nums)):

            if nums[i] in uniques:
                return True  #dupe found
            elif nums[i] not in uniques:
                uniques.append(nums[i])
            
            if len(uniques) > k:
                uniques.pop(0)
            
        return False
                
            
            
            

            
            






        