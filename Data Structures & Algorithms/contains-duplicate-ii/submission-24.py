# GREEN 2026-11-25 | alone, first submit, 20:20 | space is O(min(n, k)), not O(1) | review ~Dec 2
#rep nov 25
#
#QUESTION
#a duplicate exists
#exists within k distance under or equal k
#
#APPROACH
#so this seems like a sliding window question
#k is the max length of the window
#if a dupe exists within k distance we can early return true
#if the k window slides all the way to the end and no dupes are found then return a false
#use two pointers for left and right side of the window
#for the window itself use a set so traking dupes we can use the in keyword and its O(1)
#
#TIME: O(n) gotta slide through all elements
#SPACE: O(1) because the set is as big as k


# WALKTHROUGH
# k=3
# 1 2 3 1
# l
#       r
# window=1,2,3

# 2 1 2
#   l
#       r

# window = 1, 2


# Solved: 20:20 

class Solution:

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        window = set()
        l = 0
        r = 0

        while r < len(nums):

            if abs(r - l) > k:
                window.remove(nums[l])
                l += 1

            if nums[r] not in window:   #initially had the order wrong, i did this check before the abs(r-l) check, after stepping through 2,1,2 i fixed it
                window.add(nums[r])
            elif nums[r] in window:
                return True
            
            r += 1
        
        return False
        

        