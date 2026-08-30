class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq={}
        flag=False
        visit=set()
        for pre,cor in prerequisites:
            print((pre,cor))
            if pre in prereq:
                prereq[pre].append(cor)
            else:
                prereq[pre]=[cor]

        print(prereq)
        for i in range(numCourses):
            if i in prereq:
                print(i,prereq[i],"THIS")
                for pre in prereq[i]:
                
                    if self.dfs(pre,visit,prereq) :
                        continue
                    else:
                        return False      
        return True
    def dfs(self,val,visit,prereq):
        print (val,type(val))
        if val not in prereq:
            return True
        if val in visit:
            return False 
        visit.add(val)
        for pre in prereq[val]:
            self.dfs(pre,visit,prereq)
        visit.remove(val)
        return
    
        

