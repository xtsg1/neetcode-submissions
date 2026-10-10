from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        for n in nums:
            freq_map[n] += 1
        
        count_list = []
        for n, f in freq_map.items():
            count_list.append((f, n))
        count_list.sort(reverse=True)

        output = []
        for i in range(k):
            output.append(count_list[i][1])
        
        return output







        