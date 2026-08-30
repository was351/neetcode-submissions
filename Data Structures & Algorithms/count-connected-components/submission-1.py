from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph=defaultdict(list)
        counter=0
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visit=set()
        path=set()
        for i in range(n):
            if i not in visit:
                self.dfs(i,graph,visit,path)
                counter+=1
        return counter
    def dfs(self,node,graph,visit,path,parent=None):
        if node in path:
            return True
        if node in visit:
            return False 
        path.add(node)
        for val in graph[node]:
            if val !=parent:
                if not self.dfs(val,graph,visit,path,node):
                    return False
        path.remove(node)
        visit.add(node)
        return True
        
                    
            
