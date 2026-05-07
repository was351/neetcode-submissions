class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counter1= {}
        counter2={}
        for letter in s1:
            counter1[letter] = counter1.get(letter, 0) + 1

        l=0
        for r in range(len(s2)):
            counter2[s2[r]] = counter2.get(s2[r], 0) + 1
            
            while r-l+1>=len(s1) :
                if counter2 == counter1:
                    return True
                counter2[s2[l]] -= 1
                if counter2[s2[l]] == 0:
                    del counter2[s2[l]]
                l+=1
            
    
        return False
            
        