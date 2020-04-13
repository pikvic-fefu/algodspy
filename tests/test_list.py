import unittest

from algodspy.list import List


class TestList(unittest.TestCase):
    def test_list(self):
        data = [1, 2, 3]
        lst = List(data)
        self.assertEqual(lst.data, data)

    def test_list_get_item(self):
        data = [1, 2, 3]
        lst = List(data)
        self.assertEqual(lst.get_item(1), data[1])

    def test_list_repr(self):
        data = [1, 2, 3]
        lst = List(data)
        self.assertEqual(lst.__repr__(), data.__repr__())
        


if __name__ == '__main__':
    unittest.main()