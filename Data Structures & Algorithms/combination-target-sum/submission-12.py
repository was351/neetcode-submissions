class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        cur=[]
        res=[]
        self.rec(0,cur,res,nums,target)
        return res
    
    def rec(self,i,cur,res,nums,target):
        if target==0:
            res.append(cur.copy())
            return 
       
        if i>=len(nums) or target<0:
            return 
        cur.append(nums[i])
        target-=nums[i]
        self.rec(i,cur,res,nums,target)
        cur.pop()
        target+=nums[i]
        self.rec(i+1,cur,res,nums,target)
        return


        