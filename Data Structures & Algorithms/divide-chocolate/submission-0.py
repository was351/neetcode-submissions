class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        l=min(sweetness)
        r=sum(sweetness)//(k+1)
        while l<r:
            mid=(l+r+1)//2

            if self.sweetness(mid,sweetness)>=k+1:
                l=mid
            else:
                r=mid-1
        return l
            
    def sweetness(self,n,sweetness):
        count=0
        cur=0
        for sweet in sweetness:
            cur+=sweet
            if cur>=n:
                count+=1
                cur=0
        return count

            