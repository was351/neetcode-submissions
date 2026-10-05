class Solution:
    def climbStairs(self, n: int) -> int:
        cache={}
        return self.rec(n,cache)
    

    def rec(self,n,cache):
        if n<=2:
            return n
        if n in cache:
            return cache[n]
        cache[n]=self.rec(n-1,cache)+self.rec(n-2,cache)
        
        return cache[n]
        