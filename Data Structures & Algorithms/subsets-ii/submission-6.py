class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        seen=set()
        cur=[]
        res=[]
        nums.sort()
        self.rec(0,cur,seen,res,nums)
        return res

    def rec(self,i,cur,seen,res,nums):
        if i==len(nums):
            new=tuple(cur)
            if new not in seen:
                res.append(cur.copy())
                seen.add(new)
            return
        if i>=len(nums):
            return 
        cur.append(nums[i])
        self.rec(i+1,cur,seen,res,nums)
        cur.pop()
        self.rec(i+1,cur,seen,res,nums)
        return 