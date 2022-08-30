import unittest
from logics import can_move, get_empty_list, get_index_from_number, get_number_from_index, is_zero_in_mas, move_down, move_left, move_up

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
    
    def test_9(self):
        mas = [
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
        ]
        self.assertEqual(is_zero_in_mas(mas), False)
    
    def test_10(self):
        mas = [
            [0, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
            [1, 1, 1, 1],
        ]
        self.assertEqual(is_zero_in_mas(mas), True)

    def test_11(self):
        mas = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
        self.assertEqual(is_zero_in_mas(mas), True)

    def test_12(self):
        mas = [
            [2, 2, 0, 0],
            [0, 4, 4, 0],
            [0, 0, 2, 2],
            [0, 0, 0, 2],
        ]
        rez = [
            [4, 0, 0, 0],
            [8, 0, 0, 0],
            [4, 0, 0, 0],
            [2, 0, 0, 0],
        ]
        self.assertEqual(move_left(mas), (rez, 16))

    def test_13(self):
        mas = [
            [2, 2, 4, 4],
            [0, 4, 4, 2],
            [8, 8, 2, 2],
            [2, 2, 2, 2],
        ]
        rez = [
            [4, 8, 0, 0],
            [8, 2, 0, 0],
            [16, 4, 0, 0],
            [4, 4, 0, 0],
        ]
        self.assertEqual(move_left(mas), (rez, 48))
    
    def test_14(self):
        mas = [
            [2, 2, 2, 2],
            [2, 2, 4, 0],
            [4, 2, 4, 0],
            [4, 2, 2, 2],
        ]
        rez = [
            [4, 4, 2, 4],
            [8, 4, 8, 0],
            [0, 0, 2, 0],
            [0, 0, 0, 0],
        ]
        self.assertEqual(move_up(mas), (rez,32))

    def test_15(self):
        mas = [
            [2, 2, 2, 2],
            [2, 2, 4, 0],
            [4, 2, 4, 0],
            [4, 2, 2, 2],
        ]
        rez = [
            [0, 0, 0, 0],
            [0, 0, 2, 0],
            [4, 4, 8, 0],
            [8, 4, 2, 4],
        ]
        self.assertEqual(move_down(mas), (rez, 32)) 

    def test_16(self):
        mas = [
            [2, 4, 2, 4],
            [4, 2, 4, 2],
            [2, 4, 2, 4],
            [2, 2, 4, 2],
        ]
        self.assertEqual(move_down(mas), True) 

    def test_17(self):
        mas = [
            [2, 4, 2, 4],
            [4, 2, 4, 2],
            [2, 4, 2, 4],
            [4, 2, 4, 2],
        ]
        self.assertEqual(can_move(mas), False) 

if __name__ == 'main':#if ide not pycharm
    unittest.main()