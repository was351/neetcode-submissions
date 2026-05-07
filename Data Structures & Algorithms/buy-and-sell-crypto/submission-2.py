class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      b=0
      bp=prices[b]
      profit=0
      for s in range (len(prices)):
        profit=max(profit,prices[s]-prices[b])
        if prices[s]<bp:
            b=s
            bp=prices[s]
      return profit
            

