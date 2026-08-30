class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for val in asteroids:
            if stack:
                if stack[-1]<0 and val>0 or stack[-1]>0 and val<0 :
                    check=stack.pop()
                    if abs(check) == abs(val):
                        continue 
                    elif abs(check)>abs(val):
                        stack.append(check)
                        continue 
                    else:
                        stack.append(val)
                        continue 
            stack.append(val)
        return stack
        