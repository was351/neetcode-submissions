
class ListNode:
    def __init__(self,key:int,value:int):
        self.key=key
        self.val=value
        self.prev=None
        self.next=None
    
class LinkedList:
    def __init__(self):
        self.head=ListNode(0,0)
        self.tail=ListNode(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head
    def add(self,node):
        temp=self.head.next
        self.head.next=node
        node.prev=self.head
        temp.prev=node
        node.next=temp
    def remove(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev


class LRUCache:

    def __init__(self, capacity: int):
        self.nodemap={}
        self.keyL=LinkedList()
        self.capacity=capacity
        self.size=0


    def get(self, key: int) -> int:
        if self.nodemap.get(key):
            cur=self.nodemap[key]
            self.move_to_front(cur)
            return cur.val
        
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if self.nodemap.get(key):
            cur=self.nodemap[key]
            cur.val=value
            self.move_to_front(cur)
            
        
        else:
            new=ListNode(key,value)
            self.nodemap[key]=new
            self.keyL.add(new)
            if self.size<self.capacity:
                self.size+=1
            else:
                cur=self.keyL.tail.prev
                del self.nodemap[cur.key]
                self.keyL.remove(cur)
        return


    def move_to_front(self,node):
        self.keyL.remove(node)
        self.keyL.add(node)


        
