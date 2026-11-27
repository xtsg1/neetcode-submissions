# rep nov 27

# APPROACH
# use one pointer
# keep track of the lowest seen
# find profit of max over lowest
# keep track of highest profit ever recorded
# thats it!


class Solution:

    def maxProfit(self, prices: List[int]) -> int:

        lowest = prices[0]
        profitable = 0
        for p in prices:

            lowest = min(p, lowest)
            profit = p - lowest
            profitable = max(profitable, profit)
        
        return profitable
        