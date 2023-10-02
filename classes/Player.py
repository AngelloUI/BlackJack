class Player:
    def __init__(self):
        self.cards = []
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
        num_of_aces = 0
        for card in self.cards:
            if isinstance(card.value,list):
                sum_of_card_values += card.value[1]
                num_of_aces += 1
            else:
                sum_of_card_values += card.value
        while num_of_aces > 0 and sum_of_card_values > 21:
            sum_of_card_values -= 10  # Если сумма больше 21 и есть туз, считаем туз как 1 очко
            num_of_aces -= 1
        return sum_of_card_values

