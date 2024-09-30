class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profits = [0]
        for i in range(1, len(prices)):
            profits.append(prices[i] - prices[i - 1])
        profit = 0
        for i in range(len(profits)):
            if profits[i] > 0:
                profit += profits[i]
        return profit