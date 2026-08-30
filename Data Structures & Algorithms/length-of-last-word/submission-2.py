class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.split(" ")
        count=0
        word=s[-1]
        print(s[-1])
        for i in word:
            count+=1
        return count