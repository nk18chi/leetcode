import unittest
import importlib
f = importlib.import_module('solutions.771_jewels_and_stones.index')


class Test(unittest.TestCase):
    def test_numJewelsInStones(self):
        test_patterns = [
            ("aA", "aAAbbbb", 3),
            ("z", "ZZ", 0),
        ]

        for i, (arg1, arg2, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = f.Solution()
                self.assertEqual(s.numJewelsInStones(arg1, arg2), expected)


if __name__ == '__main__':
    unittest.main()