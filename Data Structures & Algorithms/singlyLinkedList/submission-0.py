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

    def remove(self, index: int) -> bool:
        i=0
        cur=self.head
        if index==0:
            cur=self.head
            if cur.next is not None:
                self.head=cur.next
            else:
                self.head=None
        while i < index-1 and cur.next:
            cur = cur.next
            i += 1
            if not cur.next:
                return False
        cur.next=cur.next.next
        if cur.next ==None:
            self.tail=cur
        return True
                        

    def getValues(self) -> List[int]:
        cur=self.head
        val=[]
        while cur is not None:
            val.append(cur.val)
            cur=cur.next
        return val




