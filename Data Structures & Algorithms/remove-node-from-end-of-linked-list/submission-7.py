# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ahead=head
        i=0
        if head.next is None:
            return head.next
        
        while i<n+1 and ahead :
            ahead=ahead.next
            i+=1
        
        remove=head 
        if ahead==None:
            head.next=None
            return head

        while ahead:
            ahead=ahead.next
            remove=remove.next
        remove.next=remove.next.next
        return head
