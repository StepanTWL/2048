from typing import List, Tuple
import random

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

def move_left(arr: List[List[int]]) -> Tuple[List[List[int]], int]:
    delta=0
    for row in arr:
        while 0 in row:
            row.remove(0)
        while not len(row)==4:
            row.append(0)
    for i in range(4):
        for j in range(3):
            if arr[i][j] == arr[i][j+1] and arr[i][j]:
                arr[i][j]*=2
                delta+=arr[i][j]
                arr[i].pop(j+1)
                arr[i].append(0)
    return arr,delta


def move_right(arr: List[List[int]]) -> Tuple[List[List[int]], int]:
    delta=0
    for row in arr:
        while 0 in row:
            row.remove(0)
        while not len(row)==4:
            row.insert(0,0)
    for i in range(4):
        for j in range(3,0,-1):
            if arr[i][j] == arr[i][j-1] and arr[i][j]:
                arr[i][j]*=2
                delta+=arr[i][j]
                arr[i].pop(j-1)
                arr[i].insert(0,0)
    return arr,delta

def move_up(arr: List[List[int]]) -> Tuple[List[List[int]], int]:
    delta=0
    for j in range(4):
        column = []
        for i in range(4):
            if arr[i][j]:
                column.append(arr[i][j])
        while not len(column)==4:
            column.append(0)
        for i in range(3):
            if column[i] == column[i+1] and column[i]:
                column[i]*=2
                delta+=column[i]
                column.pop(i+1)
                column.append(0)
        for i in range(4):
            arr[i][j] = column[i]
    return arr,delta

def move_down(arr: List[List[int]]) -> Tuple[List[List[int]], int]:
    delta=0
    for j in range(4):
        column = []
        for i in range(4):
            if arr[i][j]:
                column.append(arr[i][j])
        while not len(column)==4:
            column.insert(0,0)
        for i in range(3,0,-1):
            if column[i] == column[i-1] and column[i]:
                column[i]*=2
                delta+=column[i]
                column.pop(i-1)
                column.insert(0,0)
        for i in range(4):
            arr[i][j] = column[i]
    return arr,delta

def can_move(arr: List[List[int]]) -> bool:
    for i in range(3):
        for j in range(3):
            if arr[i][j]==arr[i][j+1] or arr[i][j]==arr[i+1][j]:
                return True
    return False