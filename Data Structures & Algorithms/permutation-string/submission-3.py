class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq={}
        for l in s1:
            freq[l]=freq.get(l,0)+1
        count=len(s1)
      
        print (freq)
        l=0
        for r in range(len(s2)):
            if r-l+1>len(s1):
                print(s2[l])
                l_val= freq.get(s2[l])
                print(l_val)
                if l_val==0:
                        count+=1
                        freq[s2[l]]=l_val+1
                l+=1
            print(s2[r],count)
            if s2[r] in freq:
                freq[s2[r]]=freq.get(s2[r])-1
                if freq[s2[r]]==0:
                    count-=1
                if count==0:
                    return True 

        return False 
        