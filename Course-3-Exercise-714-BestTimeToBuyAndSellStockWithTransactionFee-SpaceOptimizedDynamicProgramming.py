from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        hold, free = -prices[0], 0

        for i in range(1, n):
            tmp = hold
            hold = max(hold, free - prices[i])
            free = max(free, tmp + prices[i] - fee)

        return free


if __name__ == '__main__':

    # Inputs and Expected Outputs
    prices_1 = [1, 3, 2, 8, 4, 9]
    fee_1 = 2
    expected_output_1 = 8
    prices_2 = [1, 3, 7, 5, 10, 3]
    fee_2 = 3
    expected_output_2 = 6

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.maxProfit(prices_1, fee_1)
    test_2 = solution_2.maxProfit(prices_2, fee_2)

    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")