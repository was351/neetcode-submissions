# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dum=ListNode(0)
        add=dum
        while l1 and l2:
            if l1.val>l2.val:
                add.next=l2
                l2=l2.next
                add=add.next

            else:
                add.next=l1
                l1=l1.next
                add=add.next
        if l1:
            add.next=l1
        if l2:
            add.next=l2
        return dum.next