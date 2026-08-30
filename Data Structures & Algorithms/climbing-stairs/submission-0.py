class Solution:
    def climbStairs(self, n: int) -> int:
        res=[]
        path=[]
        self.rec(n)
        return len(res)
    def rec(self,n):
        if n <= 2:
            return n
        return self.rec(n-1)+rec(n-2)
        


            

