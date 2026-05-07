class Solution:
    def countSubstrings(self, s: str) -> int:
        count=0
        for r in range(len(s)):
            for i in range (r+1):
                if self.ispali(i,r,s):
                    count+=1

        return count 

    def ispali(self,l,r,arr):

        while l<r:
            if arr[l]==arr[r]:
                l+=1
                r-=1
            else:
                return False
        return True




