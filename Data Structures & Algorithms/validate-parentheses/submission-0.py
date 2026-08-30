class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')': '(', '}': '{', ']': '['}
        #partner = mapping[char]
        mem = []
        for char in s: 
            if char in mapping:
                if mem: 
                    t = mem.pop()
                    if t == mapping[char]:
                        continue
                    else:
                        return False
                else: 
                    return False 
            else:
                mem.append(char)

    
        return True






        

