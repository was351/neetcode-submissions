class Solution:
    def isValid(self, s: str) -> bool:
        match={')':'(',"}":"{","]":"["}
        brackets=s.split()
        seen=[]
        for char in s:
            if char in match:
                if not seen:
                    return False
                check=seen.pop()
                if check !=match[char]:
                    return False
                
            else:
                seen.append(char)
        return len(seen)==0