# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.recurse(head,None)
    def recurse(self,node,prev):
        if not node:
            head=prev
            return prev
        temp=node.next
        node.next=prev
        return self.recurse(temp,node)
        