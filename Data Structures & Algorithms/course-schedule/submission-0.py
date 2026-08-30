class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq={}
        flag=False
        for pre,cor in prerequisites:
            print((pre,cor))
            if pre in prereq:
                prereq[pre].append(cor)
            else:
                prereq[pre]=[cor]
        print(prereq)
        for i in range(numCourses):
            if i in prereq:
                continue
            else:
                print(i)
                flag=True
                break
        return flag