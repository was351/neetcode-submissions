class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need={}
        for letter in s1:
            need[letter]=need.get(letter,0)+1
        l=0
        zero=len(need)
        for r in range(len(s2)):
            if (r-l>=len(s1)):
                if need.get(s2[l])==0:
                    zero+=1
                if s2[l] in need:
                    need[s2[l]]+=1
                    if need.get(s2[l])==0:
                        zero-=1
                l+=1
            if s2[r]in need:
                if need[s2[r]]==0:
                    zero+=1

                need[s2[r]]-=1
                
                if need[s2[r]]==0:
                    zero-=1
                    if zero==0:
                        return True
                
        return False 


        