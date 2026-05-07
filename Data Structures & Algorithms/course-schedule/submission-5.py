class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq={}
        flag=False
        visit=set()
        safe=set()
        for pre,cor in prerequisites:

            if pre in prereq:
                prereq[pre].append(cor)
            else:
                prereq[pre]=[cor]

        print(prereq)
        for i in range(numCourses):
            if i in prereq:
                if self.dfs(i,visit,prereq,safe) :
                    continue
                else:
                    return False      
        return True
    def dfs(self,val,visit,prereq,safe):
        if val not in prereq:
            safe.add(val)
            return True
        if val in safe:
            return True
        if val in visit:
            return False 
        visit.add(val)
        for pre in prereq[val]:
            if not self.dfs(pre,visit,prereq,safe):
                return False
        visit.remove(val)
        safe.add(val)
        return True
