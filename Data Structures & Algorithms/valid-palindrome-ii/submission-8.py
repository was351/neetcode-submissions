class Solution:
    def validPalindrome(self, s: str) -> bool:
            l=0
            r=len(s)-1
            flag=True
            while l<r:
                print({s[r]},"r")
                print({s[l]},"l")
                if s[r]==s[l]:
                    r-=1
                    l+=1
                    continue
                elif s[r]!= s[l] and flag:
                    if s[r]==s[l+1]:
                        l+=1
                        flag=False
                        continue
                    if s[r-1]==s[l]:
                        r-=1
                        flag=False
                        continue
                    else:
                        return False

                else:
                    return False
            return True