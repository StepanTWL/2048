import random
import sys
from typing import List, 
import pygame


column = 4
row = 4
mas = [[0]*column for i in range(row)]

def pretty_print(arr: List[List[int]]):
    for row in arr:
        print(*row)

def get_number_from_index(i: int,j: int) -> int:
    return i*column+j+1

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
    for i in range(row):
        for j in range(column):
            if mas[i][j]==0:
                empty.append(get_number_from_index(i,j))
    return empty

WHITE = (255, 255, 255)
GREY = (127, 127, 127)

BLOCKS = 4
SIZE_BLOCK = 100
MARGIN = 10
WIDTH = BLOCKS*SIZE_BLOCK + (BLOCKS + 1) * MARGIN
HEIGTH = WIDTH + SIZE_BLOCK
TITLE_REC = pygame.Rect(0, 0, WIDTH, SIZE_BLOCK)


pretty_print(mas)
print(get_empty_list(mas))


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption('2048')


while is_zero_in_mas(mas):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            pygame.draw.rect(screen, WHITE, TITLE_REC)
            for row in range(BLOCKS):
                for column in range(BLOCKS):
                    w = column*SIZE_BLOCK+(column+1)*MARGIN
                    h = row*SIZE_BLOCK+(row+1)*MARGIN + SIZE_BLOCK
                    pygame.draw.rect(screen, GREY, (w, h, SIZE_BLOCK, SIZE_BLOCK))
            empty = get_empty_list(mas)
            random.shuffle(empty)
            random_num = empty.pop()
            x, y = get_index_from_number(random_num)
            mas = insert_2_or_4(mas, x, y)
            print(f'Мы заполнили элемент под номером {random_num}')
            pretty_print(mas)
    pygame.display.update()
