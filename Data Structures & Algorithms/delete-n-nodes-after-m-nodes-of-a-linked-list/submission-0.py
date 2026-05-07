# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        tail=dummy
        i=0
        cur=head
        while cur:
            if i<m:
                temp=cur.next
                cur.next=None
                tail.next=cur
                tail=tail.next
                cur=temp
            elif i<n+m:
                cur=cur.next
            i+=1
            if i>n+m+1:
                i=0
        return dummy.next
                
            


        