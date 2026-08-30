class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights) 
        r=sum(weights)
        while l<r:
            mid=(l+r)//2
            d=0
            belt=0
            for cargo in weights:
                belt+=cargo
                if belt>mid:
                    belt=cargo
                    d+=1
            if d<=days:
                r=mid
            else:
                l=mid+1
        return l