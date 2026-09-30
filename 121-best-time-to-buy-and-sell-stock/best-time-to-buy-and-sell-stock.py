class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxprofit=0
        min_price = prices[0]
        for price in prices:
            if price<min_price:
                min_price = price
            else:
                maxprofit = max(maxprofit, price-min_price)
        return maxprofit