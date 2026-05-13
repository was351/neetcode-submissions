class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        cur=[]
        res=[]
        self.cur(0,cur,res,nums)
        return res
    


    def cur(self,i,cur,res,nums):
        if i >= len(nums):
            res.append(cur.copy())
            return
        for num in nums:
            if num not in cur:
                cur.append(num)
                self.cur(i+1,cur,res,nums)
                cur.pop()
        
        