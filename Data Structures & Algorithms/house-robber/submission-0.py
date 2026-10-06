class Solution:
    def rob(self, nums: List[int]) -> int:
        cache={}
        return self.calc(len(nums)-1,nums,cache)
    
    def calc(self,n,nums,cache):
        if n<0:
            return 0
        if n==0:
            return nums[0]
        if n==1:
            return max(nums[1],nums[0])
        if n in cache:
            return cache[n]
        skip=self.calc((n-1),nums,cache)

        take=self.calc((n-2),nums,cache)+nums[n]
        cache[n]=max(skip,take)
        return cache[n]