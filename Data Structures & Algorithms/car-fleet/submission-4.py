class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=list(zip(position,speed))
        cars.sort(reverse=True)
        stack=[]
        for i in range (len (cars)):
            if not stack or (target-cars[i][0])/cars[i][1]>stack[-1]:
                stack.append((target-cars[i][0])/cars[i][1])


            
        return len(stack)
