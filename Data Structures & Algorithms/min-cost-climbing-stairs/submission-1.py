class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache={}
        return self.rec(len(cost),cost,cache)
    
    def rec(self,i,cost,cache):
        if i<2:
            return 0
        if i in cache:
            return cache[i]
        
        cache[i]=min(self.rec(i-1,cost,cache)+cost[i-1],self.rec(i-2,cost,cache)+cost[i-2])
        return cache[i]

        