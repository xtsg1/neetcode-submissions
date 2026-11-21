# rep nov 21

# QUESTION
# return the k most frequent
# any order

# APPROACH
# we need to make a count dictionary for nums
# then take the top k elements
# but how to get top k? since dict are not sorted by frequency
# instead of dict we init empty list of len(nums) in theory the largest is 1,1,1,1,1,1...
# each number index is the frequency in which a number appears
# so this means we have to build the dict first

# time: build dict -> assign to boxes -> loop again all O(n)
# space: store a dict, boxes, also O(n)

# walkthrough
# 1 2 2 3 3 3 4 4 
# counts = {1:1, 2:2, 3:3, 4:2}
# freqs = [[], [1], [2, 4], [3]]
# freqs = [[3], [2, 4], [1], []]
# topk = 3
# res = [3, 2, 4]

class Solution:
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # create count dict
        counts = {} # n: ct
        for n in nums:
            counts[n] = counts.get(n, 0) + 1 #inits+adds
        
        # assign to boxes
        max_ct = max(counts.values())
        freqs = [[] for _ in range(max_ct + 1)] # range is exclusive so if max is 3, range needs to be 0:2+1 = 3
        for n, ct in counts.items():
            freqs[ct].append(n) 

        # reverse freqs (most to least), i guess i can reverse loop here too
        freqs = freqs[::-1]
        
        #gather top k
        res = []
        i = 0
        while k:
            if freqs[i]:
                res.extend(freqs[i])
                k -= len(freqs[i])
            i += 1
        
        return res

            
            


            


        