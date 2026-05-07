import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        freq={}
        heap=[]
   
        res=[]
        last_letter=None
        if len(s)<=1:
            return s

        for letter in s:
            freq[letter]=freq.get(letter,0)+1
            
               
        for key,val in freq.items():
            heapq.heappush(heap,(-val,key))
        while len(heap)>0:
            temp=heapq.heappop(heap)
            if len(res) == 0 or res[-1] != temp[1]:
                res.append(temp[1])
                temp_count, temp_char = temp
                new_temp = (temp_count + 1, temp_char)
                if last_letter:
                    heapq.heappush(heap,last_letter)
                last_letter = new_temp if new_temp[0] < 0 else None
            else:
                return ""
            
        return "".join(res) if len(res)==len(s)else""