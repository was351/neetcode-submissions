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
        j=i
        while j+1<len(nums) and nums[j]==nums[j+1]:
            j+=1
        self.sub(j+1,cur,res,nums)
       
        

           
        
        

        
