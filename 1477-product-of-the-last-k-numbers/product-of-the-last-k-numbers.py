class ProductOfNumbers:

    def __init__(self):
        self.arr = []
        self.arrprod =[1]

    def add(self, num: int) -> None:
        self.arr.append(num)
        if num == 0:
            self.arrprod = [1]
        else:
            self.arrprod.append(num * self.arrprod[-1])

    def getProduct(self, k: int) -> int:
        if k + 1 > len(self.arrprod):
            return 0
        else:
            return self.arrprod[-1] // self.arrprod[-1-k]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)