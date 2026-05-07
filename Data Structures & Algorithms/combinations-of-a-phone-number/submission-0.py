class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        cur=[]
        res=[]
        dig=[]
        val={2:['a','b','c'],3:['d','e','f'],4:['g','h','i'],5:['j','k','l'],6:['m','n','o'],7:['p','q','r','s'],8:['t','u','v'],9:['w','x','y','z']}
        if len(digits)<1:
            return[]

        "".split(digits)
        for s in digits:

            dig.append(int(s))

       
        self.comb(0,dig,cur,res,val)
        return res

    def comb(self,i,dig,cur,res,val):
        if len(cur)>=len(dig):
            res.append("".join(cur))
            return
        for letter in val[dig[i]]:
            cur.append(letter)
            self.comb(i+1,dig,cur,res,val)
            cur.pop()
        return 

    
    
        
        
