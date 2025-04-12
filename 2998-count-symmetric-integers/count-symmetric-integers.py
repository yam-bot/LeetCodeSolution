class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        num1 , num2, count = 0, 0, 0
        for n in range(low,high+1):
            strn = str(n)
            l = len(strn)
            if l & 1 == 1 : continue
            if l == 2 : 
                num1 = n % 10
                num2 = n // 10
                if num1 == num2 : 
                    count += 1
            elif l == 4:
                num1 = n % 100
                num2 = n // 100
                num1list = [int(i) for i in str(num1)]
                num2list = [int(i) for i in str(num2)]
                if sum(num1list) == sum(num2list) : 
                    count+= 1
        return count

                        