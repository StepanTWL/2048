from typing import List, Tuple
import random
import pygame

def pretty_print(arr: List[List[int]]):
    for row in arr:
        print(*row)

def get_number_from_index(i: int,j: int) -> int:
    return i*4+j+1

def get_index_from_number(num: int) -> Tuple[int]:
    num -= 1
    x, y = num//4, num%4
    return x, y

def insert_2_or_4(arr: List[List[int]], x: int, y: int) -> List[List[int]]:
    if random.random() <= 0.75:
        arr[x][y] = 2
    else:
        arr[x][y] = 4
    return arr

def get_empty_list(arr: List[List[int]]) -> List[int]:
    empty = []
    for i in range(4):
        for j in range(4):
            if arr[i][j]==0:
                empty.append(get_number_from_index(i,j))
    return empty

def is_zero_in_mas(arr: List[List[int]]) -> bool:
    for row in arr:
        if 0 in row:
            return True
    return False