class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        curset=[]
        res=[]
        nums.sort()
        self.sub(0,curset,res,nums)
        return res

    def sub(self,i,cur,res,nums):
        if i>=len(nums): 
            res.append(cur.copy())
            return
        
        cur.append(nums[i])
        
        print(cur)
        self.sub(i+1,cur,res,nums)
        cur.pop()
        self.sub(i+1,cur,res,nums)
        while i+1<=len(nums) and nums[i]==nums[i+1]:
            i+=1
        self.sub(j+1,cur,res,nums)
        

           
        
        

        
