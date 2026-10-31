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

# start by finding the max profit of the highest sell
# then cycle the left side through and find the lowest buy

# time: O(n^2) because requires two loops
# space complexity O(1) just one extra var needed to track largest profit time

# WALK
# 10 1 5 6 7 1
#  l         r


# brute force solution 10:21
# 

class Solution:

    def maxProfit(self, prices: List[int]) -> int:


        cheapest = prices[0]
        best = 0


        for i in range(len(prices)):
            if prices[i] > cheapest:
                profit = prices[i] - cheapest
                best = max(best, profit)
            cheapest = min(cheapest, prices[i])
        
        return best

        