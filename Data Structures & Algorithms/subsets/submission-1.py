class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        cur=[]      
        self.rec(0,nums,ans,cur)
        return ans
    
    def rec(self,i,arr,res,cur):
        if i>= len(arr):
            res.append(cur.copy())
            return
        cur.append(arr[i])
        self.rec(i+1,arr,res,cur)
        cur.pop()
        self.rec(i+1,arr,res,cur)
        return

        
        