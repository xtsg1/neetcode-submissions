# rep oct 31

# QUESTION
# each element price per day
# order matters
# return max profit

# APPROACH
# a sliding window
# its like 2 pointers but the window dynamically changes based on some condition
# there are validity conditions for the window
# validity (profitable) means sell number is higher than buy
# valid windows get their profits captured and stored
# invalid windows must be slid
# 

# WALK
# 10 1 5 6 7 1
#      l r


class Solution:

    def maxProfit(self, prices: List[int]) -> int:

        largest = 0

        for l in range(len(prices) - 1):
            for r in range(l, len(prices)):

                profit = prices[r] - prices[l]
                largest = max(largest, profit)
        
        return largest

        