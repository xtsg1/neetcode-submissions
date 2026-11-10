# rep nov 10

# Approach
# order numbers by frequency in which they appear
# one way is to count and sort - O(nlogn)
# can we get to O(n)?
# one way is for each frequency, we store the numbers that appear that many times within it
# most frequent is len of nums
# this way we have a limited set of frequencies
# and we can get the most k

# time: O(n)
# space: O(n)


# WALKTHROUGH
# 1 2 2 3 3 3

# {1:1, 2:2, 3:3}

# 0 0 0 0 0 0
#   1 2 3
# 0 0 3 2 1 0

# [3 2]


# solved in 19:22

class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # make a count dict
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1

        # convert to list of freqs
        freqs = [[] for _ in range(len(nums) + 1)] # init empty freq list
        for n, ct in counts.items():
            freqs[ct].append(n)

        # reverse freqs so most frequent are at beginning
        freqs = freqs[::-1]

        # build result
        res = []
        i = 0
        while k > 0:
            if freqs[i]:
                res.extend(freqs[i])
                n_elements = len(freqs[i])
                k -= n_elements
            i += 1
        
        return res





            



        