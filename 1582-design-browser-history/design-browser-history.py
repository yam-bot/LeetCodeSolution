class NodeList:
    def __init__(self,val,prev = None, nxt = None):
        self.val = val
        self.prev = prev
        self.nxt = nxt

class BrowserHistory:

    def __init__(self, homepage: str):
        #self.fwd , self.bwd = NodeList(0), NodeList(0)
        #self.bwd, self.fwd, self.homepagenode = NodeList(0), NodeList(0) , NodeList(homepage)
        self.homepagenode = NodeList(homepage)
        #self.bwd.nxt = self.homepagenode
        #self.homepagenode.prev = self.bwd
        #self.homepagenode.nxt = self.fwd
        #self.fwd.prev = self.homepagenode
        self.curr = self.homepagenode

    def printnode(self,head):
        curr = head
        while curr:
            print(curr.val,end = " ")
            curr = curr.nxt


    def visit(self, url: str) -> None:
        newurl = NodeList(url,self.curr)
        #self.fwd.prev.nxt = currurl
        #currurl.prev = self.fwd.prev
        #currurl.nxt = self.fwd
        #self.fwd.prev = currurl
        #self.curr = currurl
        #self.printnode(self.bwd.nxt)
        self.curr.nxt = newurl
        self.curr = newurl

    def back(self, steps: int) -> str:
        for i in range(steps):
            if not self.curr.prev:
                return self.curr.val
            self.curr = self.curr.prev
        return self.curr.val

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if not self.curr.nxt:
                return self.curr.val
            self.curr = self.curr.nxt
        return self.curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)