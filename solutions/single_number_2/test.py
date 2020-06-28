import unittest
import solutions.single_number_2.index as main


class Test(unittest.TestCase):
    def test_singleNumber(self):
        test_patterns = [
            ([2, 2, 3, 2], 3),
            ([0, 1, 0, 1, 0, 1, 99], 99)
        ]

        for i, (arg, expected) in enumerate(test_patterns):
            with self.subTest(test=i):
                s = main.Solution()
                self.assertEqual(s.singleNumber(arg), expected)


if __name__ == '__main__':
    unittest.main()