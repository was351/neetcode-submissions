class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.keys = {}
        self.dummy = ListNode(0, 0)
        self.tail = self.dummy
        self.capacity = capacity
        self.size = 0


    # ---------- Helpers ----------

    def _remove(self, node):
        if node == self.tail:
            self.tail = node.prev
        node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        node.prev = None
        node.next = None

    def _insert_front(self, node):
        node.next = self.dummy.next
        if self.dummy.next:
            self.dummy.next.prev = node
        self.dummy.next = node
        node.prev = self.dummy
        if self.tail == self.dummy:
            self.tail = node


    # ---------- Get ----------

    def get(self, key: int) -> int:
        if key not in self.keys:
            return -1

        node = self.keys[key]
        self._remove(node)
        self._insert_front(node)
        return node.val


    # ---------- Put ----------

    def put(self, key: int, value: int) -> None:

        # Update existing
        if key in self.keys:
            node = self.keys[key]
            node.val = value
            self._remove(node)
            self._insert_front(node)
            return

        # Evict if full
        if self.size == self.capacity:
            lru = self.tail
            del self.keys[lru.key]
            self._remove(lru)
            self.size -= 1

        # Insert new
        new = ListNode(key, value)
        self.keys[key] = new
        self._insert_front(new)
        self.size += 1



        
