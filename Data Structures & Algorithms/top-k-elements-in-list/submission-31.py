
# rep oct 28

# Approach
# return list of k most frequent elements
# first idea is a count dictionary
# then reverse keys values into tuples
# sort it 
# grab the top k


class Solution:

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        counts = {}  # n:ct
        for n in nums:
           counts[n] = counts.get(n, 0) + 1  
        
        tuples = []
        for n, ct in counts.items():
            t = (ct, n)
            tuples.append(t)

        tuples.sort(reverse=True)

        outputs = []
        for i in range(0, k):
            element = tuples[i][1]
            outputs.append(element)
            
        return outputs







        