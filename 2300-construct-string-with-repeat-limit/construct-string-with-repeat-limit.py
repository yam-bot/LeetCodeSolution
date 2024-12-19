class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        h = [(-(ord(char)),cnt) for char, cnt in Counter(s).items()]      
        heapq.heapify(h)
        repeatLimitedString = ""
        while h:
            char, cnt = heapq.heappop(h)
            curr_char = chr(-(char))
            curr_cnt = min(cnt,repeatLimit)
            repeatLimitedString += curr_char * curr_cnt
            if cnt - curr_cnt > 0 and h:
                next_char , next_cnt = heapq.heappop(h)
                next_char = chr(-(next_char))
                repeatLimitedString += next_char
                if next_cnt > 1:
                    heapq.heappush(h,(-ord(next_char),next_cnt-1))
                heapq.heappush(h,(-ord(curr_char),cnt - curr_cnt))
        return repeatLimitedString