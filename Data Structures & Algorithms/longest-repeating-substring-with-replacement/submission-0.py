class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        counter={}
        longest=0
        for r in range(len(s)):
            if s[r] not in counter:
                counter[s[r]]=1
            else:
                counter[s[r]]+=1
            highest=max(counter.values())
            if(r-l+1>(highest+k)):
                counter[s[l]]-=1
                l+=1
            longest=max(longest,r-l+1)
        return longest
            
                
            