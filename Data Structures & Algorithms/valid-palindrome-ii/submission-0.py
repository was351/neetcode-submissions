class Solution:
    def validPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        flag=True
        while l<r:
            print(r)
            if s[r]==s[l]:
                r-=1
                l+=1
                continue
            if s[r]!= s[l] and flag:
                r-=1
                l+=1
                flag=False
                continue
            else:
                return False
        return True