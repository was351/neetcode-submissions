class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prefix =[1]*n
        postfix =[1]*n
        result = [1]*n
        pre=1
        post=1
        for i in range(1,len(nums)):
            pre=pre*nums[i]
            prefix[i]=pre
            
            
        
        for i in range(n-2,-1,-1):
            post=post*nums[i]
            postfix[i]=post
            
        
        for i in range(len(nums)):

            result[i]=prefix[i]*postfix[i]
        return result
    


           
                