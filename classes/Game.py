import random
import pygame
from classes.Card import Card
from classes.Player import Player


class Game:
    cards = [
        [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, [1, 11]],  # hearts
        [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, [1, 11]],  # clubs
        [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, [1, 11]],  # spades
        [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, [1, 11]]   # diamonds
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

    def _public_play_game(self, screen):
        player = Player()
        diler = Player()

        diler._public_add_card(self._public_give_card())
        self._public_show_card(screen, diler.cards[-1], False, self.x_diler_coordinate, self.y_diler_coordinate)
        self.x_diler_coordinate += 90

        diler._public_add_card(self._public_give_card())
        self._public_show_card(screen, diler.cards[-1], True, self.x_diler_coordinate, self.y_diler_coordinate)
        self.x_diler_coordinate += 90

        player._public_add_card(self._public_give_card())
        self._public_show_card(screen, player.cards[-1], True, self.x_player_coordinate, self.y_player_coordinate)
        self.x_player_coordinate += 90

        player._public_add_card(self._public_give_card())
        self._public_show_card(screen, player.cards[-1], True, self.x_player_coordinate, self.y_player_coordinate)
        self.x_player_coordinate += 90

        '''
        # Загрузка изображения кнопки
        add_button = pygame.image.load("img/buttons/add_button.xcf")

        # Определение позиции кнопки
        add_rect = add_button.get_rect()
        screen.blit(add_button, add_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Левая кнопка мыши
                if add_rect.collidepoint(event.pos):
                    print("add")

        '''


        for used in self.list_of_used_cards:
            print(used)
