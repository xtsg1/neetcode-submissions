# rep nov 11

# APPROACH
# use a set - by definition is unique elements
# if the length of the set is shorter than length of nums
# that means deuplication happened
# which means not every element is unique
# return bool

# time: the 'in' operator is O(1), len is O(1) too i believe so whole thing is O(1)
# space: requires O(n) in worst case if set is as large as nums

class Solution:

    def hasDuplicate(self, nums: List[int]) -> bool:

        nset = set(nums)
        return len(nset) != len(nums)

        