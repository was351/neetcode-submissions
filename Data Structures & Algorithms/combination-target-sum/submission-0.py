class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        cur=[]
        res=[]
        self.comb(0,nums,cur,res,target)
        return res
    def comb(self,i,arr,cur,res,total):
        now=sum(cur)
        print(cur)
        print(res,"res")
        if now==total:
            res.append(cur.copy())
            return
        
        print(i)
        if now>total:
            return  
        for j in range(i,len(arr)):
            cur.append(arr[j])
            self.comb(j,arr,cur,res,total)
            cur.pop()
     
        