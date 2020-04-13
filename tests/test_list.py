import unittest

from algodspy.list import List


class TestList(unittest.TestCase):
    def test_list(self):
        data = [1, 2, 3]
        lst = List(data)
        self.assertEqual(lst.data, data)

if __name__ == '__main__':
    unittest.main()