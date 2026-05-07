class Solution:
    def calPoints(self, operations: List[str]) -> int:
        total=[]
        for val in operations:
            if val=="D":
                new=total[-1]*2
                total.append(new)
            elif val=="+":
                n1=total[-1]
                n2=total[-2]
                total.append(n1+n2)
            elif val=="C":
                total.pop()
            else:
                total.append(int(val))
        return sum(total)

