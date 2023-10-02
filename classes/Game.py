import random
import pygame
from classes.Card import Card
from classes.Player import Player


class Game:
    cards = [
        [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, [1, 11]],  # hearts
        [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, [1, 11]],  # clubs
        [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, [1, 11]],  # spades
        [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, [1, 11]]  # diamonds
    ]
    list_of_used_cards = []

    x_diler_coordinate = 50
    y_diler_coordinate = 100
    x_player_coordinate = 50
    y_player_coordinate = 300

    def _public_give_card(self):
        i = random.randint(0, 3)
        j = random.randint(0, 12)
        while [i, j] in self.list_of_used_cards:
            i = random.randint(0, 3)
            j = random.randint(0, 12)
        self.list_of_used_cards.append([i, j])
        temp_add_zero = ""
        if j < 10:
            temp_add_zero = "0";
        print(f"img/cards/{i}{temp_add_zero}{j}.xcf")
        return Card(self.cards[i][j], f"img/cards/{i}{temp_add_zero}{j}.xcf")

    def _public_show_card(self, screen, card, is_opened, x, y):
        card_image = pygame.image.load(card._public_get_img_path())
        if not is_opened:
            card_image = pygame.image.load("img/cards/oblozka.xcf")
        screen.blit(card_image, (x, y))
        pygame.display.update()

    def _public_show_results(img_path):
        window_width = 400
        window_height = 300
        pygame.time.delay(3000)
        screen = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption("результат")
        background_image = pygame.image.load(img_path)
        screen.blit(background_image, (0, 0))


