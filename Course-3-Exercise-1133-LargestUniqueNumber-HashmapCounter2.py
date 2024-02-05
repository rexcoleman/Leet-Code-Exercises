from collections import defaultdict, Counter
from typing import List


class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:

        integer_count = Counter(nums).items()
        return max((v for v, c in Counter(nums).items() if c == 1), default = -1)


if __name__ == '__main__':

    # Inputs and Expected Outputs
    nums_1 = [5, 7, 3, 9, 4, 9, 8, 3, 1]
    expected_output_1 = 8
    nums_2 = [9, 9, 8, 8]
    expected_output_2 = -1


    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.largestUniqueNumber(nums_1)
    test_2 = solution_2.largestUniqueNumber(nums_2)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")