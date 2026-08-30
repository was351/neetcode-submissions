class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        tree={}
        visit=set()
        valid=set()
        if len(edges)!=n-1:
            return False 
        for start,end in edges:
            if start not in tree:
                tree[start]=[end]
            else:
                if end in tree:
                    return False
                tree[start].append(end)
                tree[end].append(start)
        for i in range(n):
            if  self.dfs(i,tree,valid,visit):
                continue
            else:
                return False
        return True
    def  dfs(self,i,tree,valid,visit):
        if i in visit:
            return False
        if i in valid:
            return True 
        print(i)
        visit.add(i)
        nodes=tree.get(i,[])
        for val in nodes:
            print(val,"hey")
            self.dfs(val,tree,valid,visit)

        visit.remove(i)
        valid.add(i)
        return True 
         



            
        