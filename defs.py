import pygame


def net(scr):  # Функция рисует сетку на фоне
    pygame.draw.line(scr, (0, 0, 0), (100, 0), (100, 300), 3)
    pygame.draw.line(scr, (0, 0, 0), (200, 0), (200, 300), 3)
    pygame.draw.line(scr, (0, 0, 0), (0, 100), (300, 100), 3)
    pygame.draw.line(scr, (0, 0, 0), (0, 200), (300, 200), 3)


def draw_ttt(scr, items):  # Функция рисует фигуры
    for i in range(3):
        for j in range(3):
            if items[i][j] == '0':
                pygame.draw.circle(scr, (255, 0, 0), (j * 100 + 50, i * 100 + 50), 45)
            elif items[i][j] == 'X':
                pygame.draw.line(scr, (128, 128, 128), (j * 100 + 5, i * 100 + 5), (j * 100 + 95, i * 100 + 95), 3)
                pygame.draw.line(scr, (128, 128, 128), (j * 100 + 95, i * 100 + 5), (j * 100 + 5, i * 100 + 95), 3)


def check_win(table, figure):  # Функция проверяет победу той или иной фигуры
    win = False
    for line in table:
        if line.count(figure) == 3:
            win = True
    for i in range(3):
        if table[0][i] == table[1][i] == table[2][i] == figure:
            win = True
    if table[0][0] == table[1][1] == table[2][2] == figure:
        win = True
    if table[0][2] == table[1][1] == table[2][0] == figure:
        win = True
    return win

