from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # we must count and confirm that this is possible
        fresh=0
        queue=deque()
        visit=set()
        #adds in all the values 
        for i in range(len(grid)):
            for j in range (len(grid[0])):
                if grid[i][j]==2:
                    queue.append((i,j))
                    visit.add((i,j))
                #counts fresh fruits 
                elif grid[i][j]==1:
                    fresh+=1
        count=0
        time=0
        #return early if no fresh fruits 
        if count==fresh:
            return time

        while queue:
            if count==fresh:
                    return time
            for _ in range(len(queue)):
                curx,cury=queue.popleft()
                neighbours=[[0,1],[1,0],[-1,0],[0,-1]]
                for dx,dy in neighbours:
                    newx=curx+dx
                    newy=cury+dy
                    if 0<=newx<len(grid) and 0<=newy<len(grid[0]) and (newx,newy) not in visit and grid[newx][newy]==1:
                        queue.append((newx,newy))
                        visit.add((newx,newy))
                        count+=1
            time+=1

        return -1

        [2,1,1]
        [2,1,2]
        [0,2,2]