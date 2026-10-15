class Solution:
    def rob(self, nums: List[int]) -> int:
        cache={}
        if len(nums)==1:
            return nums[0]
        take=self.rec(len(nums)-1,nums,True,cache)
        skip=self.rec(len(nums)-2,nums,False,cache)
        return max(take,skip)


    def rec(self,i,nums,take,cache):
        if i<0:
            return 0
        if i==1:
            if take:
                return nums[1]
            else:
                return max(nums[0],nums[1])
        if i==0:
            if take:
                return 0
            else:
                return nums[0]
        if (i, take) in cache:
            return cache[(i, take)]
        choose=nums[i]+self.rec(i-2,nums,take,cache)
        skip=self.rec(i-1,nums,take,cache)
        cache[(i, take)]=max(choose,skip)
        return cache[(i, take)]