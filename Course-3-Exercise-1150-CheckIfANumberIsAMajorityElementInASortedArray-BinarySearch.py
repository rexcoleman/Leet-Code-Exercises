import bisect
from typing import List
from collections import Counter, defaultdict


class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:

        def search(values, x):
            lo, high = 0, len(values)
            while lo < high:
                mid = (lo + high) // 2
                if values[mid] < x:
                    lo = mid + 1
                else:
                    high = mid
            return lo


        len_nums = len(nums)
        if nums[len_nums // 2] != target:
            return False
        lo = search(nums, target)
        hi = search(nums, target + 1)
        return (hi - lo) > len_nums // 2


if __name__ == '__main__':

    # Inputs and Expected Outputs
    nums_1 = [2, 4, 5, 5, 5, 5, 5, 6, 6]
    target_1 = 5
    expected_output_1 = True
    nums_2 = [10, 100, 101, 101]
    target_2 = 101
    expected_output_2 = False

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.isMajorityElement(nums_1, target_1)
    test_2 = solution_2.isMajorityElement(nums_2, target_2)

    # Print Test Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
