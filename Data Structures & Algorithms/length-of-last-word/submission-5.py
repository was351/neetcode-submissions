class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.split(" ")
        count=0
        i=len(s)-1
        while s[i] is None:
            print(s[i])
            i-=1
        word=s[i]
        print(s[-1])
        
        for i in word:
            count+=1
        return count