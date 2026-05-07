class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        cur=[]
        self.comb(1,res,cur,n,k)
        return res
    def comb(self,i,res,cur,n,k):
        if i>n+1:
            return
        if len(cur)==k:
            res.append(cur.copy())
            return 
        cur.append(i)
        self.comb(i+1,res,cur,n,k)
        cur.pop()
        self.comb(i+1,res,cur,n,k)
        return 