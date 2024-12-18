class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i,p in enumerate(prices):
            for j in prices[i+1:]:
                if j <= p : 
                    prices[i] -= j
                    break
        return prices        