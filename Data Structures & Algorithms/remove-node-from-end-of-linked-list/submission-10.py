# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        ahead=dummy.next
        i=0
        
        while i<n and ahead :
            ahead=ahead.next
            i+=1
        
        remove=dummy

        while ahead:
            ahead=ahead.next
            remove=remove.next
        remove.next=remove.next.next
        return dummy.next
