"""Unit tests for ArrayLab's array algorithms."""

import unittest

from array_utils import (
    algorithm_complexities,
    array_statistics,
    find_all_indices,
    parse_array,
    remove_duplicates,
    rotate_right,
    two_sum,
)


class TestArrayStatistics(unittest.TestCase):
    def test_positive_and_negative_numbers(self):
        self.assertEqual(
            array_statistics([3, -2, 7, 2]),
            {"min": -2, "max": 7, "sum": 10, "average": 2.5},
        )

    def test_single_number(self):
        self.assertEqual(
            array_statistics([5]),
            {"min": 5, "max": 5, "sum": 5, "average": 5.0},
        )

    def test_empty_array_raises_value_error(self):
        with self.assertRaises(ValueError):
            array_statistics([])


class TestRemoveDuplicates(unittest.TestCase):
    def test_preserves_order(self):
        self.assertEqual(remove_duplicates([3, 1, 3, 2, 1]), [3, 1, 2])

    def test_empty_array(self):
        self.assertEqual(remove_duplicates([]), [])

    def test_all_duplicates(self):
        self.assertEqual(remove_duplicates([4, 4, 4]), [4])


class TestFindAllIndices(unittest.TestCase):
    def test_multiple_matches(self):
        self.assertEqual(find_all_indices([2, 5, 2, 2], 2), [0, 2, 3])

    def test_no_matches(self):
        self.assertEqual(find_all_indices([1, 2, 3], 9), [])

    def test_empty_array(self):
        self.assertEqual(find_all_indices([], 1), [])


class TestRotateRight(unittest.TestCase):
    def test_regular_rotation(self):
        self.assertEqual(rotate_right([1, 2, 3, 4, 5], 2), [4, 5, 1, 2, 3])

    def test_k_larger_than_length(self):
        self.assertEqual(rotate_right([1, 2, 3], 5), [2, 3, 1])

    def test_zero_and_full_rotation_return_copy(self):
        values = [1, 2, 3]
        self.assertEqual(rotate_right(values, 0), values)
        self.assertEqual(rotate_right(values, 3), values)
        self.assertIsNot(rotate_right(values, 0), values)

    def test_negative_k_rotates_left(self):
        self.assertEqual(rotate_right([1, 2, 3, 4], -1), [2, 3, 4, 1])

    def test_empty_array(self):
        self.assertEqual(rotate_right([], 10), [])


class TestTwoSum(unittest.TestCase):
    def test_finds_pair(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), (0, 1))

    def test_uses_distinct_indices(self):
        self.assertEqual(two_sum([3, 3], 6), (0, 1))

    def test_no_pair(self):
        self.assertIsNone(two_sum([1, 2, 3], 10))

    def test_empty_array(self):
        self.assertIsNone(two_sum([], 0))

    def test_negative_numbers(self):
        self.assertEqual(two_sum([-4, 1, 5, 8], 4), (0, 3))


class TestInputAndComplexities(unittest.TestCase):
    def test_parse_array_spaces_commas_and_decimals(self):
        self.assertEqual(parse_array("1, 2 -3 4.5"), [1, 2, -3, 4.5])

    def test_parse_empty_array(self):
        self.assertEqual(parse_array("  "), [])

    def test_parse_invalid_value(self):
        with self.assertRaisesRegex(ValueError, "not a valid number"):
            parse_array("1 hello 3")

    def test_complexity_reference(self):
        complexities = algorithm_complexities()
        self.assertEqual(complexities["Array statistics"], ("O(n)", "O(1)"))
        self.assertEqual(complexities["Two Sum"], ("O(n) average", "O(n)"))
        self.assertEqual(len(complexities), 5)


if __name__ == "__main__":
    unittest.main()
