from collections import deque 
class Solution: 
    def islandsAndTreasure(self, grid: List[List[int]]) -> None: 
        queue=deque() 
        depth=0 
        INF=2147483647
        for i in range(len(grid)) : 
            for j in range(len(grid[0])): 
                if grid[i][j]==0: 
                    queue.append((i,j)) 
        while queue: 
            for i in range(len(queue)):
                 r,c=queue.popleft() 
                 neighbours= [0,1],[1,0],[-1,0],[0,-1] 
                 for dr,dc in neighbours:  
                    if r+dr<len(grid) and c+dc<len(grid[0]) and r+dr>=0 and c+dc>=0 and grid[r+dr][c+dc] == 2147483647:
                        queue.append((r+dr,c+dc))
                        grid[r+dr][c+dc] = grid[r][c] + 1 
            depth+=1 
        return