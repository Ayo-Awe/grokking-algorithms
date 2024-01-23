from binary_search import binary_search
import unittest


class TestBinarySearch(unittest.TestCase):
    def test_should_return_target_index(self):
        """Should correctly determine the index of the target element
        """
        arr = [0, 3, 4, 8, 19, 37, 87, 200, 490, 491, 900, 1022, 3400]
        target = 491
        target_index = 9

        idx = binary_search(arr, target)
        self.assertEqual(idx, target_index)

    def test_target_not_in_array(self):
        """Should return None since target is not in the
        array
        """
        arr = [0, 3, 4, 8, 19, 37, 87, 200, 490, 900, 1022, 3400]
        target = 5

        idx = binary_search(arr, target)

        self.assertIsNone(idx)

    def test_empty_array(self):
        """Should return None since the array is empty
        """
        arr = []
        target = 5

        idx = binary_search(arr, target)

        self.assertIsNone(idx)
