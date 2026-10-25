# already sorted
# 1 2 3 4 5 8

# 1-indexed instead of 0
# return  [i, j]
# i < j

# APPROACH
# store seen numbers, with indices (therefore hashmap)
# each new number we find the complement (target - n)
# if the complement has been seen then we have the pair
# and the two numbers will be the seen one, and the one where the complement is true
# 1-indexed


class Solution:

    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        seen = {} # number:index

        for i in range(len(numbers)):

            complement = target - numbers[i] 

            if complement in seen:
                j1 = seen[complement]+ 1
                j2 = i + 1
                return [j1, j2]

            seen[numbers[i]] = i
        