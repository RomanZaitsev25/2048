import random


def pretty_print(mas):
    print('-' * 10)
    for row in mas:
        print(*row)
    print('-' * 10)


def get_number_from_index(i, j):
    return i * 4 + j + 1


def get_index_from_number(num):
    # По числу получаем кординаты расположения в матрице. Находим номер строки,
    # А дальше номер столбца.
    num -= 1
    x, y = num // 4, num % 4
    return x, y


def insert_2_or_4(mas, x, y):
    if random.random() <= 0.75:
        mas[x][y] = 2
    else:
        mas[x][y] = 4
    return mas


def get_empty_list(mas):
    # Создаёт список и принимает пустые значения и порядковые номера при
    # помощи get_number_from_index
    empty = []
    for i in range(4):
        for j in range(4):
            if mas[i][j] == 0:
                # print(i, j)
                num = get_number_from_index(i, j)
                empty.append(num)
    return empty


def is_zero_in_mas(mas):  # если в нашем массиве нолик или нет
    for row in mas:
        if 0 in row:
            return True
    return False


def move_left(mas):
    # Данная функция будет сдвигать числа влево. Нам нужно пройтись по каждому
    # ряду массива. В ряду 2 0 0 4. 4- смещается а нули удаляются. Поэтому
    # образуется 2,4. Нам нужно после них добавить 0 до четырёх.
    delta = 0
    for row in mas:
        while 0 in row:
            row.remove(0)
        while len(row) != 4:
            row.append(0)
    for i in range(4):  # строка
        for j in range(3):  # столбец
            # Если текущее значение будет равно соседу справа и значение не 0.
            # То наш текущий элемент увеличиваем его в два раза.
            # А соседа удаляем. В этот ряд в конец лобавляем ноль.
            if mas[i][j] == mas[i][j + 1] and mas[i][j] != 0:
                mas[i][j] *= 2
                delta += mas[i][j]
                mas[i].pop(j + 1)
                mas[i].append(0)
    return mas, delta


def move_right(mas):
    delta = 0
    for row in mas:
        while 0 in row:
            row.remove(0)
        while len(row) != 4:
            row.insert(0, 0)
    for i in range(4):  # строка
        for j in range(3, 0, -1):  # столбец
            if mas[i][j] == mas[i][j - 1] and mas[i][j] != 0:
                mas[i][j] *= 2
                delta += mas[i][j]
                mas[i].pop(j - 1)
                mas[i].insert(0, 0)
    return mas, delta


def move_up(mas):
    delta = 0
    for j in range(4):
        column = []
        for i in range(4):
            if mas[i][j] != 0:
                column.append(mas[i][j])
        while len(column) != 4:
            column.append(0)
        for i in range(3):
            if column[i] == column[i + 1] and column[i] != 0:
                column[i] *= 2
                delta += column[i]
                column.pop(i + 1)
                column.append(0)
        for i in range(4):
            mas[i][j] = column[i]
    return mas, delta


def move_down(mas):
    delta = 0
    for j in range(4):
        column = []
        for i in range(4):
            if mas[i][j] != 0:
                column.append(mas[i][j])
        while len(column) != 4:
            column.insert(0, 0)
        for i in range(3, 0, -1):
            if column[i] == column[i - 1] and column[i] != 0:
                column[i] *= 2
                delta += column[i]
                column.pop(i - 1)
                column.insert(0, 0)
        for i in range(4):
            mas[i][j] = column[i]
    return mas, delta


def can_move(mas):
    # ДАвайте проверим можем ли мы двигаться в права или лево,
    # когда 2 цифры один.Или сверху в низу 2 одинаковые. ВЫбрали 3 потому
    # что будем обращаться к cоседям справа или сниз и наоборот
    for i in range(3):
        for j in range(3):
            if mas[i][j] == mas[i][j + 1] or mas[i][j] == mas[i + 1][j]:
                return True
    return False
