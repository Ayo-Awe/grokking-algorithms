from recursive_max import recursive_max
import unittest


class TestRecursiveMax(unittest.TestCase):
    def test_should_return_max_item_in_list(self):
        """Should correctly return the max iten in a list
        """
        arr = [0, 1022, 1, 2, 3400, 20, 100, 352, 289, 1]
        expected = 3400

        arr_max = recursive_max(arr)

        self.assertEqual(arr_max, expected)

    def test_should_return_none_on_empty_array(self):
        """Should return None when array is empty
        """
        arr = []

        max = recursive_max(arr)

        self.assertIsNone(max)
