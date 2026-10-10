from collections import defaultdict
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache={}
        return self.rec(amount,cache,coins)

    def rec(self,amount,cache, coins):
        if amount<0:
            return -1
        if amount==0:
            return 0
        if cache.get(amount):
                return cache[amount]
        track=0
        for coin in coins:
            attempt=1+self.rec(amount-coin,cache,coins)
            if attempt!=0:
                if cache.get(amount):
                    cache[amount]=min(cache[amount],attempt)
                    
                else:
                    cache[amount]=attempt
            else:
                track+=1
            if track==len(coins):
                cache[amount]=-1
      
        return  cache[amount]





    
    