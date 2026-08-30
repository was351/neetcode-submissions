class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        while l<r:
            print(l,r,"here")
            mid=l+(r-l)//2 # 2
            total=0
            
            for pile in piles:
                total+=math.ceil(pile/mid)
            print(total,mid,"there")
            if total<=h:
                r=mid
            else:
                l=mid-1
            return l