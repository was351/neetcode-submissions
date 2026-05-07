# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap=[]
        dummy=ListNode(0)
        add=dummy
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap,(lists[i].val,i,lists[i]))
        while heap:
            val,index,cur=heapq.heappop(heap)
            add.next=cur
            add=add.next
            if cur.next:
                cur=cur.next
                heapq.heappush(heap,(cur.val,index,cur))
        return dummy.next
            
            