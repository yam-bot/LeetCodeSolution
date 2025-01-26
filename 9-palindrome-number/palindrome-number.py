class Solution:
    def isPalindrome(self, x: int) -> bool:
        l = []
        if x < 0 : return False
        while x:
            l.append(x % 10)
            x = x // 10
            #print(l)
        if l[::-1] == l : return True
        else : return False