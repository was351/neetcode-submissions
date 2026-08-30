class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r=max(piles)
        l=1
        low=1000000
        while l<r:
            mid=l+(r-l)//2 # 2
            total=0

            for pile in piles:
                total+=math.ceil(pile/mid)
            if total>h:
                l=mid+1            
            else:
                r=mid
            low=min(r,low)
        return low