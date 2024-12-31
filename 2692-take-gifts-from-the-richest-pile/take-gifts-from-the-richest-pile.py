class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(k):
            maxpile = max(gifts)
            maxpileind = gifts.index(maxpile)
            gifts[maxpileind] = floor(sqrt(maxpile))
        return sum(gifts)
            
