import unittest
from main import get_empty_list, get_index_from_number, get_number_from_index

class Test_2048(unittest.TestCase):

    def test_1(self):
        self.assertEqual(get_number_from_index(1,2),7)
    
    def test_2(self):
        self.assertEqual(get_number_from_index(3,3),16)

    def test_3(self):
        a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
        mas = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        self.assertEqual(get_empty_list(mas), a)

    def test_4(self):
        a = [2,3,5,7,8,9,10,12,14,15]
        mas = [
            [1, 0, 0, 1],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [1, 0, 0, 1],
        ]
        self.assertEqual(get_empty_list(mas), a)

    def test_5(self):
        a = []
        mas = [
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
        ]
        self.assertEqual(get_empty_list(mas), a)
    
    def test_6(self):
        self.assertEqual(get_index_from_number(7), (1,2))
    
    def test_7(self):
        self.assertEqual(get_number_from_index(16), (3,3))

    def test_8(self):
        self.assertEqual(get_number_from_index(1), (0,0))

if __name__ == 'main':#if ide not pycharm
    unittest.main()