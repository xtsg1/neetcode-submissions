# rep october 23
class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left_products = [nums[0]] 
        for i in range(1, len(nums)):
            cumulative_product = left_products[i-1] * nums[i]
            left_products.append(cumulative_product)


        rnums = nums[::-1]
        right_products = [rnums[0]]
        for i in range(1, len(rnums)):
            cumulative_product = right_products[i-1] * rnums[i]
            right_products.append(cumulative_product)
        
        right_products = right_products[::-1]

        outputs = []
        for i in range(len(nums)):
            if i == 0:
                left = 1
                right = right_products[i+1]
            elif i == len(nums) - 1: 
                right = 1
                left = left_products[i-1]
            else:
                left = left_products[i-1]
                right = right_products[i+1]

            product = left * right
            outputs.append(product)
        
        return outputs
        

        # 1  2  4  6
# left  # 1  2  8  48
# right # 48 48  24  6






# 2 3 4 9 8 8
#     i 

# L L   R R R 

# 2 6   576 64  8


# we need a left product and a right product
# as i increments
# left product gets accumulated
# right product doesn't
        
# how can it be done in one loop?