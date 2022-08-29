import sys
from logics import *


mas = [[0]*4 for i in range(4)]

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
