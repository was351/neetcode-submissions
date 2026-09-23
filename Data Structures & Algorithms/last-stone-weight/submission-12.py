import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while heap:
            if len(heap) == 1:
                return -heap[0]

            stone1 = heapq.heappop(heap)
            stone2 = heapq.heappop(heap)

            if stone1 != stone2:
                remain = stone1 - stone2
                heapq.heappush(heap, remain)

        return 0