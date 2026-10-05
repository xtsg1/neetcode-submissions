class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq_map = {}
        for num in nums:  #gen freq map
            if num not in freq_map:
                freq_map[num] = 1
            else:
                freq_map[num] += 1
        
        print(freq_map)
        freq = list(freq_map.values())
        freq.sort(reverse=True)
        cutoff_value = freq[k-1]


        print(freq)
        print(cutoff_value)
        
        res = []
        for k, v in freq_map.items():
            if v >= cutoff_value:
                res.append(k)
        
        return res
        
        

        
        
        