class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        """Return value at given index, or -1 if out of bounds."""
        i = 0
        cur = self.head
        while i < index and cur:
            cur = cur.next
            i += 1
        return cur.val if cur else -1

    def insertHead(self, val: int) -> None:
        """Insert a new node at the beginning of the list."""
        new = Node(val)
        if not self.head:  # empty list
            self.head = new
            self.tail = new
        else:
            new.next = self.head
            self.head = new

    def insertTail(self, val: int) -> None:
        """Insert a new node at the end of the list."""
        new = Node(val)
        if not self.tail:  # empty list
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            self.tail = new
    def remove(self, index: int) -> int:
        """Remove node at index. Return 1 if successful, -1 if index invalid."""
        if not self.head:  # empty list
            return False

        if index == 0:  # remove head
            self.head = self.head.next
            if self.head is None:  # list became empty
                self.tail = None
            return 1

        cur = self.head
        i = 0
        while i < index - 1 and cur.next:
            cur = cur.next
            i += 1

        if not cur.next:  # index out of bounds
            return False

        # Remove node
        cur.next = cur.next.next

        # Update tail if needed
        if cur.next is None:
            self.tail = cur

        return True

    def getValues(self) -> List[int]:
        cur=self.head
        val=[]
        while cur is not None:
            val.append(cur.val)
            cur=cur.next
        return val




