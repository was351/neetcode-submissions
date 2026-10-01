class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        cur=[]
        res=[]
        self.create(0,cur,res,s)
        return res

    def create (self,i,cur,res,s):
        if len(cur)>=4 and i!=len(s):
            return
        if i==len(s) and len(cur)==4:
            res.append('.'.join(cur))
            return
        for j in range (1,4):
            if i+j<=len(s):
                split=s[i:i+j]
                if split[0]=='0'and len(split)>1:
                    continue 
                elif 0>int(split) or int(split)>=256:
                    continue
                else:
                    cur.append(split)
                self.create(i+j,cur,res,s)
                cur.pop()
        return 
            
        