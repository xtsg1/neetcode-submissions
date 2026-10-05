class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:

        nums = set(nums)
        print(f"set: {nums}")

        longest = 0

        for n in nums:
            if (n-1) not in nums:  # seq start
                consecutive = 1
                m = n
                while True:
                    if (m+1) in nums:
                        consecutive += 1
                        m += 1
                    else: 
                        break
                if consecutive > longest:
                    print(f"longer series found! {consecutive} > {longest}")
                    longest = consecutive
        
        print(f"Longest was {longest}")
        return longest

                


1, 2, 3, 4, 8
                
                    


            

                


            

            


        