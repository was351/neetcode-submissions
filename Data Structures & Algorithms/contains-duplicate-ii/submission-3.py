class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l=0
        check=set()
        for r in range(len(nums)):
            if (r-l)>k:
                check.remove(nums[l])
                l+=1
                
            if nums[r] in check:
                return True
            check.add(nums[r])    
        return False
            
            