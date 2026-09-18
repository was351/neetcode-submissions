class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        cur=[]
        res=[]
        self.rec(nums,cur,res)
        return res
    
    def rec(self,nums,cur,res):
        if len(cur)==len(nums):
            res.append(cur.copy())
            return 
        for i in range(len(nums)):
            if nums[i] not in cur:
                cur.append(nums[i])
                self.rec(nums,cur,res)
                cur.pop()
               
        return

        
        