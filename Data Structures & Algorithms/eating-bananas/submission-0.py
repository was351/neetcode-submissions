class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        right=max(piles)
        left=0
        
        while left<right:
           mid=left+(right-left)//2
           if mid>h/4:
                right=mid-1
           elif mid<h/4:
                left=mid+1
        if mid>0:    
            return mid-1
        else:
            return max(piles)
