class Solution:

    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        tree=collections.defaultdict(list)
        visit=set()
        path=set()
        for u,v in edges:

            tree[u].append(v)
            tree[v].append(u)
        if not self.dfs(0,-1,visit,tree,path):
            return False
        
        print(visit)
        return len(visit)==n
        
    def dfs(self,node,parent,visit,tree,path):
        if node in path:
            return False
        if node in visit:
            return True
        path.add(node)
       
        for val in tree[node]:
            if val is not parent:
                if not self.dfs(val,node,visit,tree,path):
                    return False
        path.remove(node)
        visit.add(node)
        return True

            
                

