class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = [1] * len(nums)
        product = 1
        for i in range(len(nums)):
            product *= nums[i]
            prefix[i] = product
        
        print(prefix)

        postfix = [1] * len(nums)
        product = 1
        for i in range(len(nums)-1, -1, -1):
            product *= nums[i]
            postfix[i] = product
        
        print(postfix)

        output = [1] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                pre = 1
                post = postfix[i+1]
            elif i == len(nums) - 1:
                post = 1
                pre = prefix[i-1]
            else:
                pre = prefix[i-1]
                post = postfix[i+1]
                
            product = pre * post
            output[i] = product
        
        return output




        
