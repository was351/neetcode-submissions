class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r=max(piles)
        l=1
       
        while l<r:
            total=0
            mid=l+(r-l)//2
            for val in piles:
                total+=int(math.ceil(val/mid))
            if total<=h:
                r=mid
            else:
                l=mid+1
        return l 
