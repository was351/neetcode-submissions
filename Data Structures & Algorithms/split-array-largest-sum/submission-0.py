class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l=max(nums)
        r=sum(nums)
        while l<r:
            mid=(l+r)//2
            if self.can_split(mid,nums,k):
                r=mid
            else:
                l=mid+1
        return l





    def can_split(self,largest,nums,k):
        subarray=1
        cur=0
        for num in nums:
            cur+=num
            if cur>largest:
                subarray+=1
                cur=num
        return subarray<=k


