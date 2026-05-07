class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        cur=[]
        res=[]
        self.sub(0,cur,res,nums)
        return res 
    
    def sub(self,i,cur,res,nums):
            if i>=len(nums):
                res.append(cur.copy())
                return
            cur.append(nums[i])
            print(i)
            self.sub(i+1,cur,res,nums)
            cur.pop()
            self.sub(i+1,cur,res,nums)
            return 
