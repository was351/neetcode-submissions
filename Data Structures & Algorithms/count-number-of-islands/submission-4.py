from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    count+=1
                    self.bfs(i,j,grid)

        return count 

    def bfs(self,i,j,grid):
        queue=deque()
        queue.append((i,j))
        while queue:
            for _ in range (len(queue)):
                curX,curY=queue.popleft()
                if 0<=curX<len(grid) and 0<=curY<len(grid[0]) and grid[curX][curY]=="1":
                    grid[curX][curY]="0"
                    neighbour=[[0,1],[1,0],[-1,0],[0,-1]]
                    for dx,dy in neighbour:
                        queue.append((curX+dx,curY+dy))
        return 




