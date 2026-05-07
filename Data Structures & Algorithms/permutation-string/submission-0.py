class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter1={}
        counter2={}
        for letter in s1:
            if letter in counter1:
                counter1[letter]+=1
            else:
                counter1[letter]=1
        l=0
        for r in range(len(s2)):
            if s2[r]in counter2:
                counter2[s2[r]]+=1
            else:
                counter2[s2[r]]=1
            
            while r-l+1>=len(s1) :
                if counter2 == counter1:
                    return True
                counter2[s2[l]] -= 1
                if counter2[s2[l]] == 0:
                    del counter2[s2[l]]
                l+=1
            
            r+=1
        return False
            
        