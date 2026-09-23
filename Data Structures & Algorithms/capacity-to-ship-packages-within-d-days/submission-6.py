class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        r=sum(weights)
        while l<r:
            mid=(l+r)//2
            day=1
            carry=0
            for weight in weights:
                carry+=weight
                if carry>mid:
                    day+=1
                    carry=weight
            if day>days:
                l=mid+1
            else:
                r=mid
        return l


