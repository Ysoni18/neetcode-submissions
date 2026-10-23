class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 0
        min_price = prices[0]
        maxProf = prices[right] - prices[left]

        while right < len(prices):
            if prices[right] < min_price:
                min_price = prices[right]
            
            currProfit = prices[right] - min_price

            if currProfit > maxProf:
                maxProf = currProfit
            
            right += 1
        
        return maxProf