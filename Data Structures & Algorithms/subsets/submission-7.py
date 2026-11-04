class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        cur=[]
        self.rec(0,cur,res,nums)
        return res
    
    def rec(self,i,cur,res,nums):
        if i==len(nums):
            res.append(cur.copy())
        if i>=len(nums):
            return
        cur.append(nums[i])
        self.rec(i+1,cur,res,nums)
        cur.pop()
        self.rec(i+1,cur,res,nums)
        return 

            