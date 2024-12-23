import unittest
from typing import List
from twoSum import TwoSum

class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.solution = TwoSum()

    def test_case_1(self):
        nums = [2, 7, 11, 15]
        target = 9
        self.assertEqual(self.solution.twoSum(nums, target), [0, 1])

    def test_case_2(self):
        nums = [3, 2, 4]
        target = 6
        self.assertEqual(self.solution.twoSum(nums, target), [1, 2])

    def test_case_3(self):
        nums = [3, 3]
        target = 6
        self.assertEqual(self.solution.twoSum(nums, target), [0, 1])

    def test_case_4(self):
        nums = [1, 2, 3, 4, 5]
        target = 10
        self.assertEqual(self.solution.twoSum(nums, target), [])

    def test_case_5(self):
        nums = [0, 4, 3, 0]
        target = 0
        self.assertEqual(self.solution.twoSum(nums, target), [0, 3])

    def test_case_6(self):
        nums = [-3, 4, 3, 90]
        target = 0
        self.assertEqual(self.solution.twoSum(nums, target), [0, 2])

    def test_empty_list(self):
        nums = []
        target = 5
        self.assertEqual(self.solution.twoSum(nums, target), [])

    def test_single_element(self):
        nums = [5]
        target = 5
        self.assertEqual(self.solution.twoSum(nums, target), [])

if __name__ == "__main__":
    unittest.main()
