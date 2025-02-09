class NumberContainers:

    def __init__(self):
        self.numtoind = defaultdict(SortedSet)
        self.indtonum = defaultdict(int)
        
    def change(self, index: int, number: int) -> None:
        if self.indtonum[index] and self.numtoind[self.indtonum[index]] and self.indtonum[index] != number:
            #print("number",number,"index",index,"numtoind", self.numtoind,"indtonum",self.indtonum)
            self.numtoind[self.indtonum[index]].remove(index)
        self.indtonum[index] = number
        self.numtoind[number].add(index)

    def find(self, number: int) -> int:
        if number not in self.numtoind or not self.numtoind[number]:
            return -1
        else:
            return self.numtoind[number][0]


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)