from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj=defaultdict(list)
        for i in range(len(prerequisites)):
            adj[prerequisites[i][1]].append(prerequisites[i][0])
        visit=set()
        path=set()
        def dfs(node):
            if node in path:
                return True 
            if node in visit:
                return False 
            path.add(node)
            for nei in adj[node]:
                if nei not in visit:
                    if dfs(nei):
                        return True
            path.remove(node)
            visit.add(node)
            return False
        
        for i in range(numCourses):
            if i not in visit:
                if dfs(i):
                    return False
        return True
        

            
