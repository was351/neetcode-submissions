# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.rec(None,head)
    def rec(self,prev,cur):
        if not cur:
            return prev
        temp=cur.next
        cur.next=prev
        return self.rec(cur,temp)
