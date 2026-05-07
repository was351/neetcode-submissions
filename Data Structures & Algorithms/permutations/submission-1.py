class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        cur=[]
        self.rec(0,nums,cur,res)
        return res

    def rec(self,i,nums,cur,res):
        if i>=len(nums):
            res.append(cur.copy())
            return
        for j in nums:
            if j not in cur:
                cur.append(j)
                self.rec(i+1,nums,cur,res)
                cur.pop()
