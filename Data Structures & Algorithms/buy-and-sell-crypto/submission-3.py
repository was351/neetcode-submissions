class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        local=0
        maxp=-1*int("inf")
        while r in range(1,len(prices)):
            if price[r]<price[l]:
                l=r
            max(maxp,price[r]-price[l])
        if maxp>0:
            return maxp
        return 0
        
        



