class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        vals={}
        for num in nums:
            vals[num]=vals.get(num,0)+1
        cur=[]
        res=[]
        self.rec(nums,vals,cur,res)
        return res
        
    def rec(self,nums,vals,cur,res):
        if len(cur)==len(nums):
            res.append(cur.copy())
            return 
        for value in vals:
            if vals[value]>0:
                cur.append(value)
                vals[value]-=1
                self.rec(nums,vals,cur,res)
                cur.pop()
                vals[value]+=1
               
        
