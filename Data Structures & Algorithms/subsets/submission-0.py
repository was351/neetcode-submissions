class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        cur=[]      
        self.helper(0,nums,ans,cur)
        return ans

    def helper(self,i,arr,res,cur):
        if i ==len(arr):
            res.append(cur.copy())
            return
        cur.append(arr[i])
        i+=1
        self.helper(i,arr,res,cur)
        cur.pop()
        self.helper(i,arr,res,cur)
        
        