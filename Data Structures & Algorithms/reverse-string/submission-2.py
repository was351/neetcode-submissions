class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        end=len(s)-1
        i=0
        while i < len(s) // 2:
            temp=s[i]
            s[i]=s[end-i]
            s[end-i]=temp
            i+=1
        
        