class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())
        length=len(s)
        for x in range (length):
            if (s[x]!=s[len(s)-1-x]):
                return False 
        return True 
                

