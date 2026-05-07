class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.split(" ")
        count=0
        i=len(s)-1
        while s[i] == "":
            print(s[i])
            i-=1
        word=s[i]
        
        return len(word)