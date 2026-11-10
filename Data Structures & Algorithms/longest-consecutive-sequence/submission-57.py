# rep nov 10

# QUESTION
# find longest consecutive sequence
# must be O(n)
# each element is exactly n+1 of the previous
# original array not sorted

# APPROACH
# sorting would make this easy but its O(nlogn)
# so have to do it without sorting
# we can use a set of all unique numbers
# and for each number check if n+1 is also in the set
# for numbers that have a n-1 that means they're int he middle of a consecutive sequence
# which means we can skip them
# the only numbers we need to check are beginnings of consecutive sequences so numbers without n-1
# if each n+1 exiists in the list, increment and count the length
# keep track of the longest running list

# time: O(n) in this case because each item accessed once
# space: O(n) might generate a large list as part of scratch work in finding sequence

# WALKTHROUGH

# 2 20 4 10 3 4 5

# nset: 2 3 4 5 10 20

# x = 2 3 4 5
# length = 4
# longest = 4

# SOLVED: in 11:22

class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:

        longest = 0
        nset = set(nums)

        for n in nums:
            
            # not beginning of sequence, skip
            if (n-1) in nset:
                continue
            
            x = n
            length = 1
            while (x+1) in nset:
                length += 1
                x += 1
            longest = max(longest, length)
        
        return longest

            
        