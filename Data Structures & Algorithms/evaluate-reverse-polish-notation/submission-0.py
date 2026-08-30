class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        counter=0
        for i in range (len(tokens)):
            if  tokens[i]=='+':
                a=stack.pop()
                b=stack.pop()
                res=b+a
                stack.append(res)

            elif tokens[i]=='-':
                a=stack.pop()
                b=stack.pop()
                res=b-a
                stack.append(res)

            elif tokens[i]=='*' :
                a=stack.pop()
                b=stack.pop()
                res=b*a
                stack.append(res)

            elif tokens[i]=='/':
                a=stack.pop()
                b=stack.pop()
                res=b/a
                stack.append(res)  
            else:
                stack.append(int(tokens[i]))
        return stack.pop()

              
           

        
