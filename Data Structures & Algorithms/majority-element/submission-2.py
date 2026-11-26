# rep nov 26

# QUESTION
# majority element always appears more than n/2 times in the array??
# follow up in O(1)
# first solution doesnt need it

# APPROACH
# we have to figure out which element is the majority element first
# a count dictionary and get top element is the easy solution but its O(n)
# how to optimize to O(1)? lets do O(n) first

# time O(n)
# space O(n)



class Solution:


    def majorityElement(self, nums: List[int]) -> int:

        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        reverse = {}
        for n, c in count.items():
            reverse[c] = n
        
        return reverse[max(reverse.keys())]


    
        