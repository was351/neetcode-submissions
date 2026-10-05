class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        l=0
        nums.sort()
        longest=1
        avail=k
        #we sorted it, so the left most value is atleast possible
        for r in range(1,len(nums)):
            diff=(nums[r]-nums[r-1])*(r-l)
            avail-=diff
            while avail<0:
                avail+=(nums[r]-nums[l])
                l+=1
            
            longest=max(r-l+1,longest)
        return longest 


