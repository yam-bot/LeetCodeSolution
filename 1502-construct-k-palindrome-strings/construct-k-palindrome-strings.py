class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k : return False
        count = Counter(s)
        odd = 0
        for c,n in count.items():
            if n & 1 == 1:
                odd += 1
        print(odd)
        if odd > k : return False
        else :  return True