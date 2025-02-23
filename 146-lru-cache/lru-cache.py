class Node:
    def __init__(self,key,val):
        self.val, self.key = val, key
        self.prev, self.nxt = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.lru , self.mru = Node(0,0) ,  Node(0,0)
        self.lru.nxt = self.mru
        self.mru.prev = self.lru
    # lru -> (2,3) -> (4,4) -> (6,7) -> mru
    #     <-       <-       <-
    def remove(self,node):
        #if node.nxt and node.prev:
        node.nxt.prev, node.prev.nxt = node.prev, node.nxt
        
    def insert(self,node):
        self.print_cache()
        #print("nhere",self.mru.prev.key,self.mru.prev.val,self.lru.nxt.key,self.lru.nxt.val)
        self.mru.prev.nxt = node
        node.nxt = self.mru
        node.prev = self.mru.prev
        self.mru.prev = node

    
    def print_cache(self):
        curr = self.lru
        while curr:
            curr = curr.nxt

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        #self.print_cache()
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        #print("----------",key)
        #self.print_cache()
        return self.cache[key].val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])
        if len(self.cache) > self.capacity:
            lrunode = self.lru.nxt
            self.remove(lrunode)
            #print(lrunode.val,lrunode.key,key,value)
            del self.cache[lrunode.key]



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)