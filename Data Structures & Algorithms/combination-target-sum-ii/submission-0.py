class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        cur=[]
        total=[]

        self.comb(0,candidates,cur,total,target)
        return total
    
    def comb(self,i,arr,cur,res,target):
        check=sum(cur)
        print(i)
        print(res)
        if check==target:
            cur.sort()
            if cur not in res:
                res.append(cur.copy())
            return
        if check>target:
            return
        if i>= len(arr):
            return
        for j in range(i,len(arr)):
            cur.append(arr[j])
            self.comb(j+1,arr,cur,res,target)
            cur.pop()
    
    
        return