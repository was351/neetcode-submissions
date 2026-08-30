class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=0
        r=max(piles)
        while l<r:
            mid=(l+r)//2
            hour=0
            for pile in piles:
                hour+=math.ceil(pile/mid)
            if hour <= h :
                r=mid
            else:
                l=mid+1
        return l