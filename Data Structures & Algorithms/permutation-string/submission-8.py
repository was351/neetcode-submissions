class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq={}
        count=0
        if len(s2)<len(s1):
            return False 
        for l in s1:
            freq[l]=freq.get(l,0)+1
        for keys in freq:
            count+=1
        print(count)
        l=0
        for r in range(len(s2)):
            if r-l+1>len(s1):
                if s2[l] in freq:
                    freq[s2[l]]+=1
                l+=1
            
            if s2[r]in freq:
                freq[s2[r]]-=1
                if freq[s2[r]]==0:
                    print(freq)
                    track=0
                    for keys,val in freq.items():
                        if val==0:
                            track+=1
                    print(track,count)
                    if track==count:
                        return True 
            
                        
                
                
                    

        return False 
        