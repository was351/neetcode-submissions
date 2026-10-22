from collections import deque 
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        seen=set()
        queue=deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0:
                    queue.append((i,j))
                    seen.add((i,j))
        distance=1
        while queue:
            for _ in range(len(queue)):
                curx,cury=queue.popleft()
                directions=[[1,0],[0,1],[-1,0],[0,-1]]
                for dx,dy in directions:
                    nextx=curx+dx
                    nexty=cury+dy
                    if 0<=nextx<len(grid) and 0<=nexty<len(grid[0]) and grid[nextx][nexty]>0 and (nextx,nexty)not in seen:
                        queue.append((nextx,nexty))
                        seen.add((nextx,nexty))
                        grid[nextx][nexty]=distance
            distance+=1
        return 
            
                


