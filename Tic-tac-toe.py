import pygame
import random
from defs import net, draw_ttt, check_win


screen_size = (300, 300)

window = pygame.display.set_mode(screen_size)
screen = pygame.Surface(screen_size)
pygame.display.set_caption('Tic-tac-toe')
screen.fill((48, 213, 200))
game_table = [['', '', ''],
              ['', '', ''],
              ['', '', '']]
loop = True
game_over = False
while loop:
    for action in pygame.event.get():
        if action.type == pygame.QUIT:
            loop = False
        if action.type == pygame.MOUSEBUTTONDOWN and not game_over:
            pos = pygame.mouse.get_pos()
            if game_table[pos[1] // 100][pos[0]//100] == '':
                game_table[pos[1] // 100][pos[0]//100] = 'X'
                x, y = random.randint(0, 2), random.randint(0, 2)
                while game_table[x][y] != '':
                    x, y = random.randint(0, 2), random.randint(0, 2)
                game_table[x][y] = '0'

            player_win = check_win(game_table, 'X')
            bot_win = check_win(game_table, '0')
            if player_win or bot_win:
                game_over = True
                if player_win:
                    pygame.display.set_caption('Вы победили!')
                else:
                    pygame.display.set_caption('Победил бот')
            elif game_table[0].count('X') + game_table[0].count('0') + game_table[1].count('X') + game_table[1].count('0') + \
                    game_table[2].count('X') + game_table[2].count('0') == 8:
                game_over = True
                pygame.display.set_caption('Ничья')

    draw_ttt(screen, game_table)
    net(screen)
    window.blit(screen, (0, 0))
    pygame.display.update()