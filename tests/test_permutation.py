import unittest
from atclib.permutation import Permutation


class Test(unittest.TestCase):
    def test_prev_permutation(self):
        self.assertEqual(Permutation.prev_permutation([3, 2, 1]), [3, 1, 2])
        self.assertEqual(Permutation.prev_permutation([1, 2, 3]), None)

    def test_next_permutation(self):
        self.assertEqual(Permutation.next_permutation([1, 2, 3]), [1, 3, 2])
        self.assertEqual(Permutation.next_permutation([3, 2, 1]), None)

    def test_nth_permutation(self):
        self.assertEqual(Permutation.nth_permutation([3, 1, 2]), 5)


if __name__ == "__main__":
    unittest.main()
