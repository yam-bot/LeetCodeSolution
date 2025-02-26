class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        people,richermap = len(quiet), defaultdict(list)
        for u , v in richer:
            richermap[v].append(u)
        ans = [-1 for i in range(people)]
        def findrich(p):
            quietest = p
            if ans[p] != -1:
                return ans[p]
            for r in richermap[p]:
                candidate = findrich(r)
                if quiet[candidate] < quiet[quietest]:
                    quietest = candidate
            ans[p] = quietest
            return quietest
        for i in range(people):
            findrich(i)
        return ans