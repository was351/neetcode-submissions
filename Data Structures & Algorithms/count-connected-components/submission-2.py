from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph=defaultdict(list)
        counter=0
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visit=set()
      
        for i in range(n):
            if i not in visit:
                self.dfs(i,graph,visit)
                counter+=1

        return counter

    def dfs(self,node,graph,visit,):
        visit.add(node)
        for val in graph[node]:
            if val not in visit:
                self.dfs(val,graph,visit,)
        return 
        
                    
            
