from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF=2147483647
        queue=deque()
        visit=set()
        distance=1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0:
                    queue.append((i,j))
                    visit.add((i,j))
        while queue:
            for k in range(len(queue)):
                i,j=queue.popleft()

                directions=[[1,0],[-1,0],[0,1],[0,-1]]
                for dx,dy in directions:
                    ni, nj = i+dx, j+dy
                    if 0<=ni<len(grid) and 0<=nj<len(grid[0]) and grid[ni][nj]==INF:
                        grid[ni][nj]=distance
                        queue.append((ni,nj))
                        visit.add((ni,nj))
                        
            distance+=1

                    