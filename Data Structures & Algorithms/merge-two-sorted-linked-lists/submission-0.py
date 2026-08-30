# Definition for singly-linked list.
class ListNode:
   def __init__(self, val=0, next=None):
       self.val = val
       self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1=list1
        cur2=list2
        head=ListNode()
        tail=head
        while cur1 and cur2:
            if cur1 == None:
                tail.next=cur2
            if cur2 == None:
                tail.next=cur1
            if cur1.val<=cur2.val:
                tail.next=cur1
                cur1=cur1.next
                tail=tail.next
            if cur2.val<=cur1.val:
                tail.next=cur2
                cur2=cur2.next
                tail=tail.next
            
        return head.next

                