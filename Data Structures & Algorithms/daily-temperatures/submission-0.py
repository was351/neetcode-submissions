class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[0]*len(temperatures)
        stack=[]
        for i,val in enumerate(temperatures):
            while stack and stack[-1][0]<val :
                prev_val, prev_i = stack.pop()
                result[prev_i] = i - prev_i
            stack.append((val,i))    
                     
                    
                
        return result

                       

