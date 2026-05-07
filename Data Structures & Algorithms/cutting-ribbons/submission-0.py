class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        l=1
        r=max(ribbons)
        if sum(ribbons)<k:
            return 0
        while l<r:
            mid=(l+r+1)//2
            count=0
            for val in ribbons:
                count+=val//mid
            
            if count>=k:
                l=mid
            else:
                r=mid-1
        return l