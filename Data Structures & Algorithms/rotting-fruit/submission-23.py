from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visit=set()
        queue=deque()
        count=0
        time=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    queue.append((i,j))
                    visit.add((i,j))
                elif grid[i][j]==1:
                    count+=1
        
        if count==0:
            return 0
        while queue:
            for i in range(len(queue)):
                cur=queue.popleft()
                edge=[[0,1],[1,0],[-1,0],[0,-1]]
                for dx,dy in edge:
                    
                    if len(grid)>cur[0]+dx>=0 and len(grid[0])>cur[1]+dy>=0 and grid[cur[0]+dx][cur[1]+dy]==1 and  (cur[0]+dx,cur[1]+dy) not in visit:
                               queue.append((cur[0]+dx,cur[1]+dy))
                               visit.add((cur[0]+dx,cur[1]+dy))
                               count-=1
            time+=1
        
        return time-1 if count==0 else -1