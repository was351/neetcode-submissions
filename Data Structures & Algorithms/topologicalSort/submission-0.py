from collections import defaultdict
class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        nodes=defaultdict(list)
        for edge,vert in edges:
            nodes[edge].append(vert)
        visit=set()
        finished=set()
        res=[]
        for i in range(n):
            if not self.dfs(i,visit,finished,res,nodes):
                return []
        res.reverse()
        return res if len(res)==n else []
    
    def dfs(self,node,visit,finished,res,nodes):
        if node in visit:
            return False 
        if node in finished:
            return True 
        visit.add(node)
        for edges in nodes[node]:
            if not self.dfs(edges,visit,finished,res,nodes):
                return False
            
        visit.remove(node)
        finished.add(node)
        res.append(node)
        return True 



        