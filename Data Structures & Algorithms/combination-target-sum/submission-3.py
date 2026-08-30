class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        cur,res=[],[]
        self.comb(0,cur,res,nums,target)
        return res
    def comb(self,i,cur,res,nums,target):
        if i>=len(nums):
            return 
        if target==0:
            res.append(cur.copy())
            return
        if target<0:
            return
        print(cur,nums[i])
        
        target-=nums[i]
        cur.append(nums[i])
        self.comb(i,cur,res,nums,target)
        cur.pop()
        target+=nums[i]
        self.comb(i+1,cur,res,nums,target)

        return
            

        