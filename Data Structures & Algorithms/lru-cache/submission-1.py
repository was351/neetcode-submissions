class ListNode:
    def __init__(self, val):
        self.val=val
        self.prev=None
        self.next=None
    
class LRUCache:

    def __init__(self, capacity: int):
        self.keys={}
        self.dummy=ListNode(0)
        self.tail=self.dummy
        self.counter=0
        self.max=capacity


    def get(self, key: int) -> int:
        if self.keys.get(key) is not None:

            cur=self.keys[key]
            if cur.prev !=self.dummy:
                cur.prev.next=cur.next
            else:
                return cur.val
            if cur.next:
                cur.next.prev = cur.prev
                if cur == self.tail:
                    self.tail=cur.prev
            temp=self.dummy.next
            cur.prev=self.dummy
            self.dummy.next=cur
            cur.next=temp
            temp.prev=cur
            return cur.val  
                            
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        if self.keys.get(key) is not None:
            cur=self.keys[key]
            cur.val=value
            if cur.prev !=self.dummy:
                cur.prev.next=cur.next
            else:
                return 
            if cur.next:
                cur.next.prev = cur.prev
                if cur == self.tail:
                    self.tail=cur.prev
            temp=self.dummy.next
            cur.prev=self.dummy
            self.dummy.next=cur
            cur.next=temp
            temp.prev=cur
        else:
            if self.max>self.counter:
                new=ListNode(value)
                if self.dummy==self.tail:
                    self.dummy.next=new
                    new.prev=self.dummy
                    self.tail=new
                    
                else:
                    new.next=self.dummy.next
                    self.dummy.next.prev=new
                    self.dummy.next=new
                    new.prev=self.dummy

                self.counter+=1
                return

            else:
                new=ListNode(value)
                self.keys[key]=new
                if self.dummy.next==self.tail:
                    
                    self.keys.remove[self.dummy.next]
                    self.dummy.next.prev=None
                    self.dummy.next=new
                    new.prev=self.dummy
                    self.tail=new

                    return
                else:
                    del self.keys[self.tail]
                    self.tail.prev.next=None
                    temp=self.tail.prev
                    self.tail.prev=None
                    self.tail=temp

                    temp=self.dummy.next
                    self.dummy.next=new
                    new.prev=self.dummy
                    new.next=temp

                    return





        
