class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        l=0
        r=len(s)-1
        while l<r:
            while ord("a")>ord(s[l]) or ord(s[l])>ord('z'):
                l+=1
            while ord("a")>ord(s[r]) or ord(s[r])>ord('z'):
                r-=1
            if s[r]==s[l]:
                l+=1
                r-=1
            else:
                return False
        return True
