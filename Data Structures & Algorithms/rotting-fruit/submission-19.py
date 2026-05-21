from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        count=0
        time=0
        queue=deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    count+=1
                elif grid[i][j]==2:
                    queue.append((i,j))
               
        if count==0:
            return 0 
        while queue:
            for k in range(len(queue)):
                i,j=queue.popleft()
                directions=[[1,0],[-1,0],[0,1],[0,-1]]
                for dx,dy in directions:
                    nx=i+dx
                    ny=j+dy
                    if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and grid[nx][ny]==1:
                        queue.append((nx,ny))
                        grid[nx][ny]=2
                        count-=1
                       
            if queue:
                time+=1
        return time if count==0 else -1

