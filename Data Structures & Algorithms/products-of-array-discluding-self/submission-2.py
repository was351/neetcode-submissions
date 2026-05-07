class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prefix =[1]*n
        postfix =[1]*n
        result = [1]*n
        pre=1
        post=1
        for i in range(len(nums)):
            prefix[i]=pre
            pre=pre*nums[i]
            
        
        for i in range(n-1,-1,-1):
            postfix[i]=post
            post=post*nums[i]
            
        
        for i in range(len(nums)):

            result[i]=prefix[i]*postfix[i]
        return result
    


           
                