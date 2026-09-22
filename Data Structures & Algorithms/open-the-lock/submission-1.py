from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visit=set(deadends)
        queue=deque()
        moves=0
        if '0000'not in visit:
            queue.append('0000')
            visit.add('0000')


        while queue:
            for _ in range(len(queue)):
                cur=queue.popleft()
                if cur==target:
                    return moves
                cur=list(cur)
                for i in range (len(cur)):
                    digit=int(cur[i])
                    prev_digit = (digit - 1) % 10
                    next_digit = (digit + 1) % 10
                    cur[i]=str(prev_digit)
                    prev_val="".join(cur)
                    cur[i]=str(next_digit)
                    next_val="".join(cur)
                    if next_val not in visit:
                        visit.add(next_val)
                        queue.append(next_val)
                    if prev_val not in visit:
                        visit.add(prev_val)
                        queue.append(prev_val)

                    cur[i]=str(digit)
            moves+=1
        return -1





    



    
        
