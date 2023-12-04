import copy

from aoc import utils
from aoc.y23.day04 import Card, parse_cards_grouped_by_number


def win_additional_cards(card: Card, cards: dict[int, list[Card]]):
    print(f"process card {card.card_number}")
    if len(card.my_winning_numbers) > 0:
        for i in range(1, len(card.my_winning_numbers) + 1):
            if card.card_number + i in cards.keys():
                cards[card.card_number + i].append(
                    copy.copy(cards[card.card_number + i][0])
                )


def main(input_file: str):
    cards = parse_cards_grouped_by_number(utils.read_file(input_file))
    for card_number in sorted(cards.keys()):
        for card in cards[card_number]:
            win_additional_cards(card, cards)
    total_cards = sum([len(cards[card_number]) for card_number in cards.keys()])
    print(f"You end with {total_cards} cards")
    return total_cards
