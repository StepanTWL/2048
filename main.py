import sys
import pygame
from logics import *
from database import get_best, insert_resurt


GAMERS_DB = get_best()

def draw_top_gamers():
    font_top = pygame.font.SysFont('simsun', 20)
    font_gamer = pygame.font.SysFont('simsun', 14)
    text_head = font_top.render('Best tries: ', True, ORANGE)
    screen.blit(text_head, (250, 5))
    for index, gamer in enumerate(GAMERS_DB):
        name, score = gamer
        s = f'{index+1}. {name} - {score}'
        text_gamer = font_gamer.render(s, True, ORANGE)
        screen.blit(text_gamer, (250, 25+20*index))

def draw_interface(score: int, delta: int = 0) -> None:
    pygame.draw.rect(screen, WHITE, TITLE_REC)
    font = pygame.font.SysFont('stxingkai', 70)
    font_score = pygame.font.SysFont('simsun', 48)
    font_delta = pygame.font.SysFont('simsun', 32)
    text_score = font_score.render('Score: ', True, ORANGE)
    text_score_value = font_score.render(f'{score}', True, ORANGE)
    screen.blit(text_score, (20, 27))
    screen.blit(text_score_value, (175, 27))
    if delta:
        text_delta = font_delta.render(f'+{delta}', True, ORANGE)
        screen.blit(text_delta, (170,65))
    pretty_print(mas)
    draw_top_gamers()
    for row in range(BLOCKS):
        for column in range(BLOCKS):
            value = mas[row][column]
            text = font.render(f'{value}',True,BLACK)
            w = column*SIZE_BLOCK+(column+1)*MARGIN
            h = row*SIZE_BLOCK+(row+1)*MARGIN + SIZE_BLOCK
            pygame.draw.rect(screen, COLORS[value], (w, h, SIZE_BLOCK, SIZE_BLOCK))
            if value:
                font_w, font_h = text.get_size()
                text_x = w + (SIZE_BLOCK - font_w)//2
                text_y = h + (SIZE_BLOCK - font_h)//2
                screen.blit(text, (text_x, text_y))


mas = [[0]*4 for i in range(4)]

COLORS = {
    0: (127,127,127),
    2: (255,255,255),
    4: (255,255,127),
    8: (255,255,0),
    16: (255,235,255),
    32: (255,235,127),
    64: (255,235,0),
    128: (235,255,255),
    256: (235,127,255),
    512: (235,0,255),
}

WHITE = (255, 255, 255)
GREY = (127, 127, 127)
ORANGE = (255, 127, 0)
BLACK = (0, 0, 0)

BLOCKS = 4
SIZE_BLOCK = 100
MARGIN = 10
WIDTH = BLOCKS*SIZE_BLOCK + (BLOCKS + 1) * MARGIN
HEIGTH = WIDTH + SIZE_BLOCK
TITLE_REC = pygame.Rect(0, 0, WIDTH, SIZE_BLOCK)
score = 0
USERNAME = None

pretty_print(mas)
print(get_empty_list(mas))

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption('2048')


def draw_intro():
    img2048 = pygame.image.load('start_2048.png')
    font = pygame.font.SysFont('stxingkai', 50)
    text_welcome = font.render('Welcome!', True, WHITE)
    name = 'Введите имя'
    is_find_name = False
    while not is_find_name:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    if name == 'Введите имя':
                        name = event.unicode
                    else:
                        name+=event.unicode
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif event.key == pygame.K_RETURN:
                    if len(name)>2:
                        global USERNAME
                        USERNAME = name
                        is_find_name = True
                        break

        screen.fill(BLACK)
        text_name = font.render(name, True, WHITE)
        rect_name = text_name.get_rect()
        rect_name.center = screen.get_rect().center
        screen.blit(pygame.transform.scale(img2048, [200, 200]), [10,10])
        screen.blit(text_welcome, [250, 80])
        screen.blit(text_name, rect_name)
        pygame.display.update()
    screen.fill(BLACK)

def draw_gameover():
    img2048 = pygame.image.load('start_2048.png')
    font = pygame.font.SysFont('stxingkai', 50)
    text_gameover = font.render('Game Over!', True, WHITE)
    text_score = font.render(f'Вы набрали {score}', True, WHITE)
    if len(GAMERS_DB):
        best_score = GAMERS_DB[0][1]
    else:
        best_score = 0
    if score > best_score:
        text = "Рекорд побит"
    else:
        text = f'Рекорд {best_score}'
    text_record = font.render(text, True, WHITE)
    insert_resurt(USERNAME, score)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
        screen.fill(BLACK)
        screen.blit(text_gameover, [220, 80])
        screen.blit(text_score, [30, 250])
        screen.blit(text_record, [30, 300])
        screen.blit(pygame.transform.scale(img2048, [200, 200]), [10,10])
        pygame.display.update()


draw_intro()

draw_interface(score)
pygame.display.update()

while is_zero_in_mas(mas) or can_move(mas):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.KEYDOWN:
            delta = 0
            if event.key == pygame.K_LEFT:
                mas,delta = move_left(mas)
            elif event.key == pygame.K_RIGHT:
                mas,delta = move_right(mas)
            elif event.key == pygame.K_UP:
                mas,delta = move_up(mas)
            elif event.key == pygame.K_DOWN:
                mas,delta = move_down(mas)
            score += delta
            if is_zero_in_mas(mas):
                empty = get_empty_list(mas)
                random.shuffle(empty)
                random_num = empty.pop()#esli mojno dvigat'sy v zapolnenom pole no tol'ko v opredelennuyu storonu???
                x, y = get_index_from_number(random_num)
                mas = insert_2_or_4(mas, x, y)
                print(f'Мы заполнили элемент под номером {random_num}')
            draw_interface(score, delta)
            pygame.display.update()

draw_gameover()