class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.merge(nums)
        
    def merge(self,nums):
        if len(nums)<2:
            return nums
        i=len(nums)//2
        left=self.merge(nums[:i])
        right=self.merge(nums[i:])
        return self.sort(left,right)
    def sort(self,right,left):
        l,r=0,0
        res=[]
        while r<len(right)and l<len(left):
            if left[l]>right[r]:
                res.append(right[r])
                r+=1
            else:
                res.append(left[l])
                l+=1
        if l<len(left):
            res.extend(left[l:])
        if r<len(right):
            res.extend(right[r:])
        return res