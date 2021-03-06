# Положить в массив 2 значения.
# Начало цикл игры:
#   ждать от пользователя команды
#   когда получим команду обработать масив
#   найти пустые клетки
#   если есть пустые клетки, случайно выбрать одну из них
#   и положить туда 2 или 4. Если пустые клетки закочены, game over

import pygame
from logigs import *
import sys
from database import get_best, cur, insert_result
import json
import os

GAMERS_DB = get_best()  # содержится коллекция и её нужно обойти с пом for


def draw_top_gamers():
    font_top = pygame.font.SysFont('simsum', 30)  # Главная запись
    font_gamer = pygame.font.SysFont('simsum', 24)  # размер отрисовки играков
    text_head = font_top.render('Best tries:', True, COLOR_TEXT)
    screen.blit(text_head, (280, 5))
    for index, gamer in enumerate(GAMERS_DB):
        name, score = gamer
        # создать динамический тест
        s = '{}. {} - {} '.format(index + 1, name, score)
        text_gamer = font_gamer.render(s, True, COLOR_TEXT)
        screen.blit(text_gamer, (280, 30 + 30 * index))
        print(index, name, score)


def draw_interface(score, delta=0):
    pygame.draw.rect(screen, WHITE, TITLE_REC)
    font = pygame.font.SysFont('stxingkai', 70)
    # Пишем счёт в таблице. Сначала пишем , каким будем шрифтом пользоваться.
    # Импортируем из pygame. Далее пишем текст. Далее на экран прикрепляю при
    # помощи blit, наш текс и его кардинаты. Далее заводим переменную score.
    # Далее перемемнную передовать в drow.interface. C перенной делаем так же
    # с текстом, все изменения. Далее наше значение score нжно изменять.
    font_score = pygame.font.SysFont('simsum', 48)
    font_delta = pygame.font.SysFont('simsum', 32)
    text_score = font_score.render('Score:', True, COLOR_TEXT)
    text_score_value = font_score.render('{}'.format(score), True, COLOR_TEXT)
    screen.blit(text_score, (20, 35))
    screen.blit(text_score_value, (175, 35))
    if delta > 0:
        text_delta = font_delta.render('{}+'.format(delta), True, COLOR_TEXT)
        screen.blit(text_delta, (170, 65))

    pretty_print(mas)  # отрисовка квадратов
    draw_top_gamers()
    for row in range(BLOCKS):
        for column in range(BLOCKS):
            value = mas[row][column]
            text = font.render(f'{value}', True, BLACK)
            w = column * SIZE_BLOCK + (column + 1) * MARGIN
            h = row * SIZE_BLOCK + (row + 1) * MARGIN + SIZE_BLOCK
            pygame.draw.rect(screen, COLORS[value],
                             (w, h, SIZE_BLOCK, SIZE_BLOCK))
            if value != 0:
                # Высота и ширина текста
                font_w, font_h = text.get_size()
                text_x = w + (SIZE_BLOCK - font_w) / 2
                text_y = h + (SIZE_BLOCK - font_h) / 2
                screen.blit(text, (text_x, text_y))


COLOR_TEXT = (255, 127, 0)
COLORS = {
    0: (130, 130, 130),
    2: (255, 255, 255),
    4: (255, 255, 128),
    8: (255, 255, 0),
    16: (255, 235, 255),
    32: (255, 235, 128),
    64: (255, 235, 0),
    128: (235, 255, 0),
    256: (235, 255, 128),
    512: (235, 235, 235),
    1024: (128, 0, 128),
    2048: (235, 128, 255),
}
WHITE = (255, 255, 255)
GRAY = (130, 130, 130)
BLACK = (0, 0, 0)
BLOCKS = 4
SIZE_BLOCK = 110
MARGIN = 10
WIDTH = BLOCKS * SIZE_BLOCK + (BLOCKS + 1) * MARGIN
HEIGHT = WIDTH + 110
TITLE_REC = pygame.Rect(0, 0, WIDTH, 110)  # кординаты


def init_const():
    global score, mas
    mas = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]
    # свормир.list nu, которые не заполнены
    empty = get_empty_list(mas)
    random.shuffle(empty)
    # достаём рандомно элементы из матрицы
    random_num1 = empty.pop()
    random_num2 = empty.pop()
    # нАМ НУЖНО ОПРЕДЕЛИТЬ ИНДЕКС РАНДОМНЫХ ЧИСЕЛ
    x1, y1 = get_index_from_number(random_num1)
    mas = insert_2_or_4(mas, x1, y1)
    x2, y2 = get_index_from_number(random_num2)
    mas = insert_2_or_4(mas, x2, y2)
    score = 0


mas = None
score = None
USERNAME = None

# показывает путь к файлу
path = os.getcwd()
# показывает список файлов в папке
if 'data.txt' in os.listdir():
    with open('data.txt') as file:
        # json- прочитает наш список и преобразет в словарь при помощи load
        data = json.load(file)
        mas = data['mas']
        score = data['score']
        USERNAME = data['user']
    # Определим полный путь к файлу
    full_path = os.path.join(path, 'data.txt')
    os.remove(full_path)
else:
    init_const()


print(get_empty_list(mas))
pretty_print(mas)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('2048')


def draw_intro():
    #  Отображает картинку 2048, на нашей заставке. Загржаем картинку.
    img2048 = pygame.image.load('2048_new.jpg')
    font = pygame.font.SysFont('stxingkai', 70)
    text_welcome = font.render('Welcome!', True, WHITE)
    # Выводит значение текста
    name = 'Enter the name'
    is_find_name = False

    while not is_find_name:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    if name == 'Enter the name':
                        name = event.unicode
                    else:
                        name += event.unicode
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif event.key == pygame.K_RETURN:
                    if len(name) > 2:
                        global USERNAME
                        USERNAME = name
                        is_find_name = True
                        break

        screen.fill(BLACK)
        text_name = font.render(name, True, WHITE)
        # Место расположения name, при помощи get_rect
        rect_name = text_name.get_rect()
        # Расположение по центру, вызывая атрибут center. и подменить его
        # кординатами нашего экрана
        rect_name.center = screen.get_rect().center
        # Уменьшает размер картинки.(Scale).
        screen.blit(pygame.transform.scale(img2048, [200, 200]), [10, 10])
        screen.blit(text_welcome, (230, 80))
        screen.blit(text_name, rect_name)  # Выводит текст на экран
        pygame.display.update()
    screen.fill(BLACK)


def draw_game_over():
    global USERNAME, mas, score, GAMERS_DB
    img2048 = pygame.image.load('2048_new.jpg')
    font = pygame.font.SysFont('stxingkai', 65)
    text_game_over = font.render('Game over!', True, WHITE)
    text_score = font.render('Вы набрали {}'.format(score), True, WHITE)
    best_score = GAMERS_DB[0][1]
    if score > best_score:
        text = 'Рекорд побит:'
    else:
        text = 'Рекорд игры: {}'.format(best_score)
    text_record = font.render(text, True, WHITE)
    insert_result(USERNAME, score)
    # В нем храниться список лучших результатов. Вновь должны обновить запрос
    # к базе данных.
    GAMERS_DB = get_best()
    make_desicion = False
    while not make_desicion:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                # Когда мы нажмём пробел или энтер, у нас в переменной станет
                # ТРУ,
                if event.key == pygame.K_SPACE:
                    # restart game with name
                    make_desicion = True
                    init_const()
                elif event.key == pygame.K_RETURN:
                    # restart game without name
                    USERNAME = None
                    make_desicion = True
                    init_const()
        screen.fill(BLACK)
        screen.blit(text_game_over, (220, 80))
        screen.blit(text_score, (30, 250))
        screen.blit(text_record, (30, 300))
        screen.blit(pygame.transform.scale(img2048, [200, 200]), [10, 10])
        pygame.display.update()

    screen.fill(BLACK)


draw_intro()

draw_interface(score)
pygame.display.update()

# Мы можем сохранить данный и продолжить позже играть. Для Этого создаём
# функцию, в нём словарь. Всё это сохраним в файлике. В качестве псевдонима
# напишем outfile. Наш файлик запишем в json объекта- это формат обменной
# информации. Наш файлик data, хотим сох в outfile при помощи dump(что
# сохраняем и куда сохраняем).


def save_game():
    data = {
        'user': USERNAME,
        'score': score,
        'mas': mas
    }
    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile)


def game_loop():
    global score, mas
    draw_interface(score)
    pygame.display.update()
    is_mas_move = False
    while is_zero_in_mas(mas) or can_move(mas):  # цикл обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_game()
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                delta = 0
                if event.key == pygame.K_LEFT:
                    mas, delta, is_mas_move = move_left(mas)
                elif event.key == pygame.K_RIGHT:
                    mas, delta, is_mas_move = move_right(mas)
                elif event.key == pygame.K_UP:
                    mas, delta, is_mas_move = move_up(mas)
                elif event.key == pygame.K_DOWN:
                    mas, delta, is_mas_move = move_down(mas)
                score += delta
                if is_zero_in_mas(mas) and is_mas_move:
                    # свормир.list nu, которые не заполнены
                    empty = get_empty_list(mas)
                    random.shuffle(empty)
                    # достаём рандомно элементы из матрицы
                    random_num = empty.pop()
                    # нАМ НУЖНО ОПРЕДЕЛИТЬ ИНДЕКС РАНДОМНЫХ ЧИСЕЛ
                    x, y = get_index_from_number(random_num)
                    mas = insert_2_or_4(mas, x, y)
                    print(f'Мы заполняем элемент под номером{random_num}')
                    is_mas_move = False

                draw_interface(score, delta)
                pygame.display.update()

        print(USERNAME)


while True:
    if USERNAME is None:
        draw_intro()
    game_loop()
    draw_game_over()
