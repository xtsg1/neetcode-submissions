#rep oct 21


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # step 1: make dict of counts
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1

        # step 1: reverse into a list, so we can sort it
        freqs = []
        for n, c in counts.items():
            pair = (c, n)  # reversed
            freqs.append(pair)
        
        # step 3: sort
        freqs.sort(reverse=True)  # most to least
        
        # step 4: slice topk
        topk = []
        for i in range(k):
            topk.append(freqs[i][1]) 
        
        return topk
                
            
# [(3, 3), (2, 2), (1, 1)]            
            


# {1: 1, 2: 2, 3: 3}

            
            


# 1 1 2 2 3 3 3

# chars  : a b c d
# counts : 2 4 1 1


# nums and top k most frequent
# dictionary of every character count
# sort that from most to least
# slice the top k
        

        