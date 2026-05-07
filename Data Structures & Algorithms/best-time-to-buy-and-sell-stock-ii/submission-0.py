class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit_so_far = 0
        for i in range(len(prices) - 1):
            price_today = prices[i]
            price_tomorrow = prices[i+1]

            if price_tomorrow > price_today:
                profit_so_far += price_tomorrow - price_today

        return profit_so_far