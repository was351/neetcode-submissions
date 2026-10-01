from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        queue=deque()
        visit=set()
        if grid[0][0]==1:
            return -1
        queue.append((0,0))
        visit.add((0,0))
        layer=0
        corner=False
        while queue:
                for _ in range(len(queue)):
                    lastx,lasty=queue.popleft()
                    if lastx==len(grid)-1 and lasty==len(grid[0])-1:
                        layer+=1
                        return layer
                    directions=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
                    for dx,dy in directions:
                        newx,newy=lastx+dx,lasty+dy
                        if 0<=newx<len(grid) and 0<=newy<len(grid[0]):
                            if (newx,newy) not in visit and grid[newx][newy]==0:
                                queue.append((newx,newy))
                                visit.add((newx,newy))
                layer+=1
                   
            
        return -1
                                