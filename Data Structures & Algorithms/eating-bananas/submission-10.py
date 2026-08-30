class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        while l<r:
            mid=(r+l)//2
            for pile in piles:
                hours=math.ceil(pile/mid)
            if hours>h:
               r=mid
            else:
                l=mid-1
    
        return mid