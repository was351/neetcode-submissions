class Node:
    def __init__(self,key,value):
        self.key=key
        self.val=value
        self.next=None
        self.prev=None
class LinkedList:

    def __init__(self):
        self.head= Node(None,None)
        self.tail=Node(None,None)
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
        self.size=0
        self.capacity=capacity
        self.linked=LinkedList()


    def get(self, key: int) -> int:
        if key in self.nodemap:
            self.move_to_front(self.nodemap[key])
            return self.nodemap[key].val
        else:
            return -1
        

        

    def put(self, key: int, value: int) -> None:
        if not key in self.nodemap:
            
            if self.capacity==self.size:
                rem=self.linked.tail.prev
                self.linked.remove(rem)
                del self.nodemap[rem.key]

            else:
                self.size+=1

            new=Node(key,value)
            self.nodemap[key]=new
            self.linked.add(new)

        else:

            self.nodemap[key].val=value
            self.move_to_front(self.nodemap[key])
        return 

    def move_to_front(self,node):
        self.linked.remove(node)
        self.linked.add(node)
        
        
