# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        new=ListNode(0)
        head=new
        dig=0
        while l1 or l2 or carry!=0:
            sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            if sum>=10:
                dig=sum%10
                carry=sum//10
            else:
                dig=sum
                carry=0
            new.next=ListNode(dig)
            new=new.next
            if l2:
                l2=l2.next
            if l1:
                l1=l1.next
        return head.next

