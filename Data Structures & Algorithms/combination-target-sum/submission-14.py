class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        cur=[]
        res=[]
        self.rec(0,nums,cur,res,target)
        
        return res
    
    def rec(self,i,nums,cur,res,target):
        if target==0:
            res.append(cur.copy())
            return
        if  target<0 or i>=len(nums):
            return 
        cur.append(nums[i])
        self.rec(i,nums,cur,res,target-nums[i])
        cur.pop()
        self.rec(i+1,nums,cur,res,target)
        return 
