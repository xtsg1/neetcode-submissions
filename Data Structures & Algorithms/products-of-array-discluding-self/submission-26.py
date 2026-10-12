class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left = []
        product = 1
        for i in range(len(nums)):
            left.append(product)
            product *= nums[i] 

        right = []
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            right.append(product)
            product *= nums[i]
        right.append(1)
        right.reverse()

        products = []
        for i in range(0, len(nums)):
            product = left[i] * right[i+1]
            products.append(product)

        return products



#  1, 3, 5, 7, 12, 15
#        i          