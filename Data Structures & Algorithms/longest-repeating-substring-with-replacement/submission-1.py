class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        freq={}
        max_len=k
        for r in range(len(s)):
            freq[s[r]]=freq.get(s[r],0)+1
            while r-l+1>freq[max(freq,key=freq.get)]+k:
                freq[s[l]]=freq.get(s[l],0)-1
                l+=1

            
            max_len=max(max_len,r-l+1)
        return max_len

            
            

            

            
                

        