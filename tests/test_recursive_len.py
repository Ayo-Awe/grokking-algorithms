from recursive_len import recursive_len
import unittest


class TestRecursiveLen(unittest.TestCase):
    def test_should_return_length_of_list(self):
        """Should correctly return the length of the list
        """
        arr = [0, 1022, 1, 2, 3400, 20, 100, 352, 289, 1]
        expected = len(arr)

        arr_len = recursive_len(arr)

        self.assertEqual(arr_len, expected)

    def test_should_return_zero_on_empty_array(self):
        """Should return zero when array is empty
        """
        arr = []

        max = recursive_len(arr)
        expected = 0

        self.assertEqual(max, expected)
