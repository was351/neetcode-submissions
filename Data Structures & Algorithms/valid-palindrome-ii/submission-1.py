class Solution:
    def validPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        flag=True
        while l<r:
            
            if s[r]==s[l]:
                r-=1
                l+=1
                continue
            if s[r]!= s[l] and flag:
                if s[r-1]==s[l]:
                    r-=2
                    l+=1
                    flag=False
                    continue
                elif s[r]==s[l+1]:
                    r-=1
                    l+=2
                    flag=False
                    continue
                else:
                    return False

            else:
                return False
        return True