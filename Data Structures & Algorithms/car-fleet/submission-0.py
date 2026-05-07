class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]
        sort=[]
        for i in range (len(position)):
            sort.append((position[i],speed[i]))
        sort=sorted(sort,reverse=True)
        for i in range(len(sort)):
            temp=(target-sort[i][0])/sort[i][1]
            if not stack or temp>stack[-1]:
                stack.append(temp)

        return len(stack)
            


