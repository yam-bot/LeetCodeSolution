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
        self.mru.prev.nxt = node
        node.nxt = self.mru
        node.prev = self.mru.prev
        self.mru.prev = node


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])
        if len(self.cache) > self.capacity:
            lrunode = self.lru.nxt
            self.remove(lrunode)
            del self.cache[lrunode.key]



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)