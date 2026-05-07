from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        visit=set()
        row,col=len(grid),len(grid[0])
        queue=deque()
       
        
        def bfs():
            queue.append((0,0))
            visit.add((0,0))
            if grid[0][0] == 1:
                return -1
            
            count=1
            while queue:
                for i in range(len(queue)):
                    r,c=queue.popleft()
                    print((r,c))
                    
                    if r>=row or c>=col or c<0 or r<0:
                        continue
                    if r==row-1 and c==col-1:
                        return count    
                    
                    
                    
                    neighbours=[-1,-1],[0,-1],[1,-1],[-1,0],[1,0],[-1,1],[0,1],[1,1]
                    for dr,dc in neighbours:
                        if c+dc < col and r+dr < row  and grid[r+dr][c+dc]!=1 and (r+dr,c+dc) not in visit:
                            visit.add((r+dr,c+dc))
                            queue.append((r+dr,c+dc))
                        

                count+=1
            return -1
       
        return bfs()