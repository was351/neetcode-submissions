class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        r=sum(weights)
        while l<r:
            mid=(l+r)//2
            cur=0
            day=1
            for pack in weights:
                cur+=pack
                if cur>mid:
                    day+=1
                    cur=pack
            print(mid)
            if day<=days:
                r=mid
            else:
                l=mid+1
        return l
