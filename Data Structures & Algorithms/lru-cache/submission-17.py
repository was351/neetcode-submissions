# Node class implemented, we need to be able to delete the key from the map, so we need to store that 
class Node:

    def __init__(self,key,value):
        self.next=None
        self.prev=None
        self.key=key
        self.val=value



#LinkedList Class with prebuilt functions 

class LinkedList:

    def __init__ (self):
    #creates empty linked list with dummy sentinel nodes
        self.head=Node(None,None)
        self.tail=Node(None,None)
        self.head.next=self.tail
        self.tail.prev=self.head
    # we have decided that the nodes will be built outside the function because we have to suffle the nodes around 
    def add(self,node):
        #store the old head node temporarilly
        temp=self.head.next
        self.head.next=node
        node.prev=self.head
        temp.prev=node
        node.next=temp
    
    def remove(self,node):
        #same as the add function, we will pass in nodes to move them around
        node.next.prev=node.prev
        node.prev.next=node.next
    


class LRUCache:

    def __init__(self, capacity: int):
        # we need to intialize an empty hashmap and linked list along with the capacoty of cache and current size 
        self.linked=LinkedList()
        self.nodemap={}
        self.capacity=capacity
        self.size=0
        

    def get(self, key: int) -> int:
        # for getting keys, there is only two branches, we either find the value and  move the value to the front or it doenst exist in map 
        if key not in self.nodemap:
            return -1 
        else:
            cur=self.nodemap[key]
            self.move_to_front(cur)
            return cur.val
        

    def put(self, key: int, value: int) -> None:
        # for this, there are three cases, its either in the list and we are updating, so we move it to the front, its not in the list and theres space or its not in the       
        #there is no space 
        if key in self.nodemap:
            #update the value of th key and move the value to the front 
            cur=self.nodemap[key]
            cur.val=value
            self.move_to_front(cur)
            return
        else:
            #create a new node and add to hashmap and linked list 
            new=Node(key,value)
            self.nodemap[key]=new
            self.linked.add(new)
            if self.capacity>self.size:

                self.size+=1
            else:
                #remove the value before the tail node 
                del self.nodemap[self.linked.tail.prev.key]
                self.linked.remove(self.linked.tail.prev)
                


    def move_to_front(self,node):
            self.linked.remove(node)
            self.linked.add(node)

        
