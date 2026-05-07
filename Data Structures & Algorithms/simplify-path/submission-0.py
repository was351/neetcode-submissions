class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        spaced=path.split("/")
        for section in spaced:
            if section == "..":
                if stack:
                    stack.pop()
            elif section=="":
                continue
            elif section==".":
                continue 
            elif not section:
                continue 
            else:
                
                stack.append(section)
        return "/" + "/".join(stack)
