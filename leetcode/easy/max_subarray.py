class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # try 1
        # max = -1
        # for i in range(0, len(prices)):
        #     for j in range(i+1, len(prices)):
        #         if prices[j] - prices[i] > max:
        #             max = prices[j] - prices[i]
        #             # print("Changing max to:", max)
        # if max == -1:
        #     return 0
        # else:
        #     return max

        profit = 0
        pick = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < pick:
                pick = prices[i]
            if prices[i] - pick > profit:
                profit = prices[i] - pick
        return profit
        