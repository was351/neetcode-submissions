class Solution:
    def isValid(self, s: str) -> bool:
        close={')':'(','}':"{","]":"["}
        stack=[]
        for l in s:
            if l in close:
                if len(stack) != 0 and stack[-1]==close[l]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(l)
        return len(stack) == 0
                
