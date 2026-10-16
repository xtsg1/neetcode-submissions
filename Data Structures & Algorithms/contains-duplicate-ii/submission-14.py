class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        window = set()    #init
        l = 0

        for r in range(len(nums)):

            if r - l > k:
                window.remove(nums[l])
                l += 1

            if nums[r] in window:
                return True

            window.add(nums[r])

        return False


    



        

# k = 3

# 1 2 9 8 2 4
# i 
#  +1+2+3 
#       j