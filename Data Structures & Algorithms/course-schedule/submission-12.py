from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj=defaultdict(list)
        for arr in prerequisites:
            adj[arr[1]].append(arr[0])
        visit=set()
        path=set()
        
        for i in range(numCourses):
            if self.dfs(i,adj,visit,path):

                continue
            else:
                return False 

        return True 
    def dfs(self, i, adj,visit,path):
        if i in path:
            print("this ",i)
            return False 
        if i in visit:
            return True
        path.add(i)
        for nei in adj[i]:
            if self.dfs(nei,adj,visit,path):
                continue
            else:
                return False 
        path.remove(i)
        visit.add(i)

        return True
        
