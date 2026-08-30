class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        peak=0
        l=0
        length=mountainArr.length()-1
        r=length
        while l<r:
            mid=(l+r)//2
            if mountainArr.get(mid)<mountainArr.get(mid+1):
                l=mid+1
            else:
                r=mid
        peak=l
        if mountainArr.get(peak)==target:
            return target
        l=0
        r=peak-1
        while l<=r:
            mid=(l+r)//2
            mid_val=mountainArr.get(mid)
            print("here")
            if mid_val==target:
                return mid
            elif mid_val>target:
                r=mid-1
            else:
                l=mid+1
        l=peak+1
        r=length
        while l<=r:
            mid=(l+r)//2
            mid_val=mountainArr.get(mid)
            print("here2")
            if mid_val==target:
                return mid
            elif mid_val<target:
                r=mid-1
            else:
                l=mid+1

        return -1