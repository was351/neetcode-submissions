class Solution:
    def canJump(self, nums: List[int]) -> bool:
        visit=set()
        return self.reach(0,nums,visit)
    
    def reach(self,i,nums,visit):
        if i<0 or i>=len(nums):
            return False
        if i==len(nums)-1:
            return True
        if nums[i]==0:
            return False
        if i in visit:
            return False
        
        visit.add(i)
        for j in range (1,nums[i]+1):
            if self.reach(i+j,nums,visit):
                return True
        return False