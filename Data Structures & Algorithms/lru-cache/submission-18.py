class Node:
    #implementation of node class. this stores the key value pair associated with the node
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.next=None
        self.prev=None

class LinkedList:
    #linked list class

    def __init__(self):
        self.head=Node(None,None)
        self.tail=Node(None,None)
        self.head.next=self.tail
        self.tail.prev=self.head
    

    #need a function that adds a node to the front
    def add(self,node):
        temp=self.head.next
        self.head.next=node
        node.prev=self.head
        node.next=temp
        temp.prev=node

    #need a remove function for anynode
    def remove(self,node):
        node.prev.next=node.next
        node.next.prev=node.prev



class LRUCache:

    def __init__(self, capacity: int):
        self.linked=LinkedList()
        self.nodemap={}
        self.capacity=capacity
        self.size=0
        

    def get(self, key: int) -> int:
        #this function will check if the value exists in the map and if it does it will move it to the front, if it does not, it will return -1 
        if key in self.nodemap:
            cur=self.nodemap[key]
            self.move_to_front(cur)
            return cur.val
        else:
            return -1 

        

    def put(self, key: int, value: int) -> None:
        # there are three possibillities for this function. the node either exists in the map(we will update the value and move to the front ), or it does not and we will check
        # the size and compare to capacity. if capacity is bigger than size, we will just add the node. otherwise we will need to remove the least used val form linked list and 
        if key in self.nodemap:
            #this branch will find the node in the map, update the value and move it to the front
            cur=self.nodemap[key]
            cur.val=value
            self.move_to_front(cur)
        else:
            new=Node(key,value)

            if self.capacity>self.size:
                #this side increses the size the linked list 
                self.size+=1
            else:
                #this branch evict least recently used node from hashmap and removes from linked list 
                rem=self.linked.tail.prev
                del self.nodemap[rem.key]
                self.linked.remove(rem)
            #this section adds the value to the node map and to the linked list 
            self.nodemap[key]=new
            self.linked.add(new)
        return 

    

    def move_to_front(self,node):
        #this function removes the node from current position and moves it to the front 
        self.linked.remove(node)
        self.linked.add(node)


    
        
