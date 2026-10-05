class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        #most ribbons is equal to ribbons cut to length 1which is equal to summ of array
        if sum(ribbons)<k:
            return 0
        #we can cut the number of ribbons to the min lenght: this is guarrenteed to be the least number of ribbons  if we cut to length to this then we atleast have this manny
        l=1
        r=max(ribbons)
        while l<r:
            mid=(l+r+1)//2
            count=0
            for rib in ribbons:
                count+=rib//mid

            if count>=k:
                l=mid
            else:
                r=mid-1
        return l



        