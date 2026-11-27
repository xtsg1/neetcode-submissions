# GREEN 2026-11-27 | review, 3:36, first submit | next ~Dec 18
# rep nov 27

# APPROACH
# use one pointer
# keep track of the lowest seen
# find profit of max over lowest
# keep track of highest profit ever recorded
# thats it!


# solved in 3:36

class Solution:

    def maxProfit(self, prices: List[int]) -> int:

        lowest = prices[0]
        profitable = 0
        for p in prices:

            lowest = min(p, lowest)
            profit = p - lowest
            profitable = max(profitable, profit)
        
        return profitable
        