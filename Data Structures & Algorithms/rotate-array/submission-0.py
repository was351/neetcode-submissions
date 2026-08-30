from collections import deque
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        l=0
        r=len(nums)-1
        while l<r :
            temp=nums[r]
            nums[r]=nums[l]
            nums[l]=temp
            l+=1
            r-=1
        mid=k-1
        l=0
        while l<mid:
            temp=nums[mid]
            nums[mid]=nums[l]
            nums[l]=temp
            l+=1
            mid-=1 
        mid=k
        r=len(nums)-1
        while mid<r :
            temp=nums[r]
            nums[r]=nums[mid]
            nums[mid]=temp
            mid+=1
            r-=1
        print(nums)
        return nums

        
