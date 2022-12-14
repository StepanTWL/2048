import os, sys, pygame, json
from logics import *
from database import get_best, insert_resurt

mas = [[0]*4 for i in range(4)]

COLORS = {
    0: (127,127,127),
    2: (255,255,0),
    4: (191,255,0),
    8: (127,255,0),
    16: (63,255,0),
    32: (63,255,0),
    64: (63,255,63),
    128: (63,255,127),
    256: (63,255,191),
    512: (63,255,255),
    1024: (63,191,255),
    2048: (63,127,255),
    4096: (63,63,255),
    8192: (63,0,255),
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

GAMERS_DB = get_best()

mas = None
score = None
USERNAME = None

def draw_top_gamers():
    font_top = pygame.font.SysFont('comicsansms', 20)
    font_gamer = pygame.font.SysFont('comicsansms', 14)
    text_head = font_top.render('Best tries: ', True, ORANGE)
    screen.blit(text_head, (250, 0))
    for index, gamer in enumerate(GAMERS_DB):
        name, score = gamer
        s = f'{index+1}. {name} - {score}'
        text_gamer = font_gamer.render(s, True, ORANGE)
        screen.blit(text_gamer, (250, 30+23*index))

def draw_interface(score: int, delta: int = 0) -> None:
    pygame.draw.rect(screen, WHITE, TITLE_REC)
    font = pygame.font.SysFont('comicsansms', 42)
    font_score = pygame.font.SysFont('comicsansms', 48)
    font_delta = pygame.font.SysFont('comicsansms', 28)
    text_score = font_score.render('Score: ', True, ORANGE)
    text_score_value = font_score.render(f'{score}', True, ORANGE)
    screen.blit(text_score, (20, 10))
    screen.blit(text_score_value, (175, 10))
    if delta:
        text_delta = font_delta.render(f'+{delta}', True, ORANGE)
        screen.blit(text_delta, (170,58))
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

def init_const():
    global mas, score
    mas = [[0]*4 for i in range(4)]
    empty = get_empty_list(mas)
    random.shuffle(empty)
    random_num1 = empty.pop()
    random_num2 = empty.pop()
    x1, y1 = get_index_from_number(random_num1)
    mas = insert_2_or_4(mas, x1, y1)
    x2, y2 = get_index_from_number(random_num2)
    mas = insert_2_or_4(mas, x2, y2)
    score = 0

def draw_intro():
    img2048 = pygame.image.load('start_2048.png')
    font = pygame.font.SysFont('comicsansms', 50)
    text_welcome = font.render('Welcome!', True, WHITE)
    name = '?????????????? ??????'
    is_find_name = False
    while not is_find_name:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    if name == '?????????????? ??????':
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
        screen.blit(text_welcome, [218, 70])#
        screen.blit(text_name, rect_name)
        pygame.display.update()
    screen.fill(BLACK)

def draw_gameover():
    global USERNAME, GAMERS_DB
    img2048 = pygame.image.load('start_2048.png')
    font = pygame.font.SysFont('comicsansms', 40)
    text_gameover = font.render('Game Over!', True, WHITE)
    text_score = font.render(f'???? ?????????????? - {score}', True, WHITE)
    if len(GAMERS_DB):
        best_score = GAMERS_DB[0][1]
    else:
        best_score = 0
    if score > best_score:
        text = "???????????? ??????????!!!"
    else:
        text = f'???????????? - {best_score}'
    text_record = font.render(text, True, WHITE)
    insert_resurt(USERNAME, score)
    GAMERS_DB = get_best()
    make_disicion = False
    while not make_disicion:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    make_disicion = True
                    init_const()
                elif event.key == pygame.K_RETURN:
                    USERNAME = None
                    make_disicion = True
                    init_const()
        screen.fill(BLACK)
        screen.blit(text_gameover, [220, 72])
        screen.blit(text_score, [30, 250])
        screen.blit(text_record, [30, 300])
        screen.blit(pygame.transform.scale(img2048, [200, 200]), [10,10])
        pygame.display.update()
    screen.fill(BLACK)

def save_game():
    data = {
        'user': USERNAME,
        'score': score,
        'mas': mas,
    }
    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile)

def game_loop():
    global score, mas
    draw_interface(score)
    pygame.display.update()
    is_mas_move = False
    while is_zero_in_mas(mas) or can_move(mas):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_game()
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                delta = 0
                if event.key == pygame.K_LEFT:
                    mas,delta,is_mas_move = move_left(mas)
                elif event.key == pygame.K_RIGHT:
                    mas,delta,is_mas_move = move_right(mas)
                elif event.key == pygame.K_UP:
                    mas,delta,is_mas_move = move_up(mas)
                elif event.key == pygame.K_DOWN:
                    mas,delta,is_mas_move = move_down(mas)
                score += delta
                if is_zero_in_mas(mas) and is_mas_move:
                    empty = get_empty_list(mas)
                    random.shuffle(empty)
                    random_num = empty.pop()
                    x, y = get_index_from_number(random_num)
                    mas = insert_2_or_4(mas, x, y)
                draw_interface(score, delta)
                pygame.display.update()


path = os.getcwd()
if 'data.txt' in os.listdir():
    with open('data.txt') as file:
        data = json.load(file)
        mas = data['mas']
        score = data['score']
        USERNAME = data['user']
    full_path = os.path.join(path, 'data.txt')
    os.remove(full_path)
else:
    init_const()
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption('2048')

while True:
    if USERNAME is None:
        draw_intro()
    game_loop()
    draw_gameover()