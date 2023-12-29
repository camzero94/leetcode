from typing import List
class Solution(object):
    def maxProfit(self, prices: List[int]):
        """
        :type prices: List[int]
        :rtype: int
        """
    
        profit = 0
        left = 0
        right = 1
        while right < len(prices):
            temp = prices[right] - prices[left]
            if prices[right] < prices[left]:
                left = right
                right += 1
            else:
                profit = max(profit, temp)
                right += 1
        return profit








res = Solution()
print(res.maxProfit([7,6,4,3,1]))
