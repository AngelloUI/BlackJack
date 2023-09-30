import pygame
import sys
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
                game = Game()
                game._public_play_game(screen)

            elif quit_rect.collidepoint(event.pos):
                running = False



    pygame.display.update()

pygame.quit()
sys.exit()
