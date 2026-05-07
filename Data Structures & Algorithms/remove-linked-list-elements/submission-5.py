class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        cur=dummy
        while cur.next:
            if cur.next.val!=val:
                cur=cur.next
            else:
                cur.next=cur.next.next
        return dummy.next