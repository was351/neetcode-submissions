class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        cur=[]
        self.rec(n,cur,res,0,0)
        
        return res

    def rec(self,n,cur,res,o_brac,c_brac):
        if len(cur)==2*n:
            add="".join(cur)
            res.append(add)
            return
        if o_brac<n:
            cur.append("(")
            self.rec(n,cur,res,o_brac+1,c_brac)
            cur.pop()
        if c_brac<o_brac:
            cur.append(")")
            self.rec(n,cur,res,o_brac,c_brac+1)
            cur.pop()
        
    
        return

        
