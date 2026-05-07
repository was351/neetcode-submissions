class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        cur=[]
        res=[]
        self.comb(1,n,k,cur,res)
        return res
    def comb(self,i,n,k,cur,res):
        if len(cur)==k:
            res.append(cur.copy())
            return
        if i > n:
            return
        
        for j in range(i,n+1):
            cur.append(j)
            self.comb(j+1,n,k,cur,res)
            cur.pop()
        
        
    