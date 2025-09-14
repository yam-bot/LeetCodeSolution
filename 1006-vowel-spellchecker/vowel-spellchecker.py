class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        ans = []
        dw = defaultdict(list)
        dwc = defaultdict(list)
        vowels = ['a','e','i','o','u']
        for w in wordlist:
            wstr = ""
            for c in w:
                if c.lower() not in vowels:
                    wstr += c.lower()
                else:
                    wstr += "0"
            dw[wstr].append(w)
            dwc[w.lower()].append(w)
        for q in queries:
            if q in wordlist:
                ans.append(q)
            elif q.lower() in dwc:
                ans.append(dwc[q.lower()][0])
            else:
                qstr = ""
                for c in q:
                    if c.lower() not in vowels:
                        qstr += c.lower()
                    else:
                        qstr += "0"
                if qstr in dw:
                    ans.append(dw[qstr][0])
                else:
                    ans.append("") 
        return ans

