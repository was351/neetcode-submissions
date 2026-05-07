class Solution:
    def mySqrt(self, x: int) -> int:
        l=0
        r=x
        while l<=r:
            mid=l+(r-l)//2
            if mid*mid<x:
                m=mid
                l=mid+1
                
            elif mid*mid==x:
                return mid
            else:
                r=mid-1
        return int(m)



        