class Player:
    cards = []

    def _public_add_card(self, card):
        self.cards.append(card)

    def _public_is_black_jack(self):
        sum_of_card_values = 0
        for card in self.cards:
            sum_of_card_values += card.value
        if sum_of_card_values == 21:
            return True
        return False

    def _public_count_score(self):
        sum_of_card_values = 0
        for card in self.cards:
            sum_of_card_values += card.value
        return sum_of_card_values
