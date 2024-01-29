from selection_sort import selection_sort
import unittest


class TestSelectionSort(unittest.TestCase):
    def test_should_sort_array_ascending(self):
        """Should correctly sort the array in ascending order
        """
        arr = [2, 3, 2, 1, 9, 10, 23]
        expected = [1, 2, 2, 3, 9, 10, 23]

        selection_sort(arr)

        self.assertEqual(arr, expected)
