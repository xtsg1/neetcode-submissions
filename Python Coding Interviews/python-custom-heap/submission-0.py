import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    heap = [] 
    for num in nums:
        pair = (-1*num, num)
        heapq.heappush(heap, pair)
    
    reverse_sorted = []
    while heap:
        pair = heapq.heappop(heap)
        reverse_sorted.append(pair[1])
    
    return reverse_sorted





# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
