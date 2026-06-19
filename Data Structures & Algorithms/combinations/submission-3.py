class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        cur=[]
        res=[]
        self.rec(1,cur,res,n,k)
        return res
    
    def rec(self,i,cur,res,n,k):
        if len(cur)==k:
            res.append(cur.copy())
            return
        if i>n:
            return
        cur.append(i)
        self.rec(i+1,cur,res,n,k)
        cur.pop()
        self.rec(i+1,cur,res,n,k)
        return

        
