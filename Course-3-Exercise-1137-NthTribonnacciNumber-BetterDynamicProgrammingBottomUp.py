class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 3:
            return 1 if n else 0
        a, b, c = 0, 1, 1
        for i in range(3, n + 1):
            a, b, c = b, c, (a + b + c)
        return c


if __name__ == '__main__':

    # Inputs and Expected Outputs
    n_1 = 4
    expected_output_1 = 4
    n_2 = 25
    expected_output_2 = 1389537

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.tribonacci(n_1)
    test_2 = solution_2.tribonacci(n_2)

    # Prnt Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 1 Output: {test_2} \nExpected Output: {expected_output_2}")

