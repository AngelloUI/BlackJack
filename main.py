import pygame
import sys
from classes.Player import Player
from classes.Game import Game


pygame.init()

window_width = 800
window_height = 600
screen = pygame.display.set_mode((window_width, window_height))

pygame.display.set_caption("BlackJack")
icon = pygame.image.load('img/ico.jpg')
pygame.display.set_icon(icon)

# fon
background_position = [0, 0]
background_image = pygame.image.load("img/table.xcf").convert()
screen.blit(background_image, background_position)

font = pygame.font.Font(None, 36)

label_play = font.render("Играть", True, (255, 255, 255))  # Задайте текст и цвет (белый)
play_rect = label_play.get_rect()
play_rect.center = (385, 290)  # Позиция текста на экране
screen.blit(label_play, play_rect)  # Отобразить текст

label_quit = font.render("Выйти", True, (255, 255, 255))  # Задайте текст и цвет (белый)
quit_rect = label_quit.get_rect()
quit_rect.center = (385, 340)  # Позиция текста на экране
screen.blit(label_quit, quit_rect)  # Отобразить текст

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Левая кнопка мыши
            if play_rect.collidepoint(event.pos):
                window_width = 800
                window_height = 600
                screen = pygame.display.set_mode((window_width, window_height))

                pygame.display.set_caption("BlackJack")
                icon = pygame.image.load('img/ico.jpg')
                pygame.display.set_icon(icon)

                # fon
                background_position = [0, 0]
                background_image = pygame.image.load("img/gametable.xcf").convert()
                screen.blit(background_image, background_position)

                player = Player()
                diler = Player()
                game = Game()

                # Раздача карт
                diler._public_add_card(game._public_give_card())
                game._public_show_card(screen, diler.cards[-1], False, game.x_diler_coordinate, game.y_diler_coordinate)
                game.x_diler_coordinate += 90

                diler._public_add_card(game._public_give_card())
                game._public_show_card(screen, diler.cards[-1], True, game.x_diler_coordinate, game.y_diler_coordinate)
                game.x_diler_coordinate += 90

                # Раздача карт игроку
                player._public_add_card(game._public_give_card())
                game._public_show_card(screen, player.cards[-1], True, game.x_player_coordinate,
                                       game.y_player_coordinate)
                game.x_player_coordinate += 90

                player._public_add_card(game._public_give_card())
                game._public_show_card(screen, player.cards[-1], True, game.x_player_coordinate,
                                       game.y_player_coordinate)
                game.x_player_coordinate += 90

                label_add_card = font.render("add card", True, (255, 255, 255))  # Задайте текст и цвет (белый)
                add_rect = label_add_card.get_rect()
                add_rect.center = (100, 500)  # Позиция текста на экране
                screen.blit(label_add_card, add_rect)  # Отобразить текст

                label_open_cards = font.render("open cards", True, (255, 255, 255))  # Задайте текст и цвет (белый)
                open_rect = label_open_cards.get_rect()
                open_rect.center = (250, 500)  # Позиция текста на экране
                screen.blit(label_open_cards, open_rect)  # Отобразить текст

                label_restart = font.render("restart", True, (255, 255, 255))  # Задайте текст и цвет (белый)
                restart_rect = label_restart.get_rect()
                restart_rect.center = (500, 500)  # Позиция текста на экране
                screen.blit(label_restart, restart_rect)  # Отобразить текст

            if add_rect.collidepoint(event.pos):
                player._public_add_card(game._public_give_card())
                game._public_show_card(screen, player.cards[-1], True, game.x_player_coordinate,
                                       game.y_player_coordinate)
                game.x_player_coordinate += 90
                if player._public_count_score() > 21:
                    Game._public_show_results("img/casino_win.xcf")
            if open_rect.collidepoint(event.pos):
                game._public_show_card(screen, diler.cards[0], True, 50, 100)
                while diler._public_count_score() < 17:
                    diler._public_add_card(game._public_give_card())
                    game._public_show_card(screen, diler.cards[-1], True, game.x_diler_coordinate,
                                           game.y_diler_coordinate)
                    game.x_diler_coordinate += 90

                if player._public_count_score() == diler._public_count_score() == 21:
                    print("Ничья (блэкджек обоим)")
                    Game._public_show_results("img/draws.xcf")
                elif player._public_count_score() == 21:
                    print("Игрок выигрывает (блэкджек)")
                    Game._public_show_results("img/player_win.xcf")
                elif diler._public_count_score() == 21:
                    print("Дилер выигрывает (блэкджек)")
                    Game._public_show_results("img/casino_win.xcf")
                elif player._public_count_score() > 21:
                    print("Дилер выигрывает (перебор у игрока)")
                    Game._public_show_results("img/casino_win.xcf")
                elif diler._public_count_score() > 21:
                    print("Игрок выигрывает (перебор у дилера)")
                    Game._public_show_results("img/player_win.xcf")
                elif player._public_count_score() > diler._public_count_score():
                    print("Игрок выигрывает")
                    Game._public_show_results("img/player_win.xcf")
                elif player._public_count_score() < diler._public_count_score():
                    print("Дилер выигрывает")
                    Game._public_show_results("img/casino_win.xcf")
                else:
                    print("Ничья")
                    Game._public_show_results("img/draws.xcf")
            if restart_rect.collidepoint(event.pos):
                print("restart")
            if quit_rect.collidepoint(event.pos):
                running = False
    pygame.display.update()

pygame.quit()
sys.exit()
