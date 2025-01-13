class Solution:
    def minimumLength(self, s: str) -> int:
        count = Counter(s)
        strlen = 0
        for c, n in count.items():
            if n >= 3 and n & 1 == 1:
                strlen += 1
            elif n > 3:
                strlen += 2
            else:
                strlen += n
        return strlen