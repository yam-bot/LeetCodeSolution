class Node:
    def __init__(self,idnum,expirytime):
        self.id = idnum
        self.expirytime = expirytime
        self.prev = None
        self.nxt = None

class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.tokenMap = {}
        self.head, self.tail = Node(None,None), Node(None,None)
        self.head.nxt = self.tail
        self.tail.prev = self.head

    #always insert to the tail
    def insert(self,token):
        self.tail.prev.nxt = token
        token.prev = self.tail.prev
        self.tail.prev = token
        token.nxt = self.tail

    def remove(self,token):
        token.nxt.prev = token.prev
        token.prev.nxt = token.nxt
        token.nxt, token.prev = None,None

    def generate(self, tokenId: str, currentTime: int) -> None:
        newtoken = Node(tokenId,currentTime + self.timeToLive)
        self.tokenMap[tokenId] = newtoken
        self.insert(newtoken)


    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.tokenMap:
            #expired
            if self.tokenMap[tokenId].expirytime <=  currentTime:
                self.remove(self.tokenMap[tokenId])
                del self.tokenMap[tokenId]
            else:
                #renew expiry time
                self.remove(self.tokenMap[tokenId])
                del self.tokenMap[tokenId]
                self.generate(tokenId,currentTime)

    def countUnexpiredTokens(self, currentTime: int) -> int:
        curr = self.head.nxt
        #print("countUnexpiredTokens",curr.id, curr.expirytime,currentTime)
        while curr != self.tail and curr.expirytime <= currentTime:
            #print(curr.id,currentTime)
            del self.tokenMap[curr.id]
            self.remove(curr)
            curr = self.head.nxt
        return len(self.tokenMap)
            






# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)