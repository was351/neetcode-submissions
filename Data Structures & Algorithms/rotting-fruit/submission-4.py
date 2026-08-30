from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue=deque()
        count=0
        depth=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    count+=1
                if grid[i][j]==2:
                    queue.append((i,j))
        while queue:
            
            for i in range (len(queue)):
                r,c=queue.popleft()
                
                    
                if r>=len(grid) or c>=len(grid[0]) or r<0 or c<0 :
                    continue
                
                neighbours=[-1,0],[0,-1],[1,0],[0,1]
                for dr,dc in neighbours:
                    if 0<=r+dr<len(grid) and 0<=c+dc<len(grid[0]) and grid[r+dr][c+dc]==1:
                        queue.append((r+dr,c+dc))
                        grid[r+dr][c+dc]=2
                        count-=1
         
        return depth if count==0 else -1
            
