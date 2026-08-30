class Solution:
    def search(self, nums: List[int], target: int) -> int:
        f=0
        l=len(nums)-1

        while f<=l:
            mid=f+(l-f)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                l=mid-1
            else:
                f=mid+1
        return nums

