class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people=sorted(people)
        l=0
        r=len(people)-1
        print (people)
        count=0
        while l<=r:
            print(r)
            total=people[r]+people[l]
            if total<=limit:
                count+=1
                l+=1
                r-=1
            else:
                r-=1
                count+=1
        return count
            

