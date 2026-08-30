class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        track=set()
        leng=0
        l=0
        for r in range (len(nums)):
            while nums[r]in track and l<r:
                track.remove(nums[l])
                l+=1
            diff=r-l+1
            leng=max(diff,leng)
            track.add(nums[r])
            r+=1
        if k>=leng:
            return True
        return False
            
            
            